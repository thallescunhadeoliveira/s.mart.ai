import os
import sys
import json
import time
from PIL import Image
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pymongo.collection import Collection
import ast
import unicodedata

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
from app.config import client, MODEL_ID, MODEL_ID_LITE, MODEL_ID_15, MODEL_ID_EMBEDDING



def construir_historico(chat_history, user_input):
    historico_mensagem = ""
    for speaker, message in chat_history[-6:]:  # últimas 6 mensagens, para não crescer demais
        if speaker == "Você":
            historico_mensagem += f"Usuário: {message}\n"
        else:
            historico_mensagem += f"s.mart.at: {message}\n"
    historico_mensagem += f"Usuário: {user_input}\n"
    historico_mensagem += "s.mart.at: "
    return historico_mensagem


def pegar_arquivo(image_path: str):

    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Erro: A imagem '{image_path}' não foi encontrada.")
        exit()

    with open(image_path, "rb") as image_file:
        # print(image_file)
        image_data = image_file.read()
    
    return image_data


def formata_json(texto: str) -> str:
    texto_ajustado = texto.split("```json\n")[1]
    texto_ajustado = texto_ajustado.split("\n```")[0]
    texto_dict = json.loads(texto_ajustado)
    return texto_dict

def converte_float(valor: str) -> float:
    try:
        return float(valor.replace(",", "."))
    except:
        return None

def converte_embedding(texto: str):
    # print(texto)
    from models.agents import Agents  
    try:
        novo_agente = Agents(client, MODEL_ID_EMBEDDING)
        embedding = novo_agente.agente_embedding(texto, "RETRIEVAL_DOCUMENT")
    except Exception as e:
        print(f"{e}: Falha no agente de embedding")
        embedding = None
    # print(embedding)
    return embedding


def formata_registro(dicionario_compras: dict) -> list:
    #criar função par definir id
    from models.agents import Agents  
    agents = Agents(client,MODEL_ID_LITE)  

    compra_id = str(int(time.time()*1000000))
    _created = datetime.now(timezone.utc)
    nova_compra = []
    modelos_fallback = [MODEL_ID_15, MODEL_ID]
    numero_modelo = 0
    i = 0
    for item in dicionario_compras['itens_comprados']:
        # print(f"Item{i}: {item}")
        i  += 1
        try:
            produto = agents.agente_formatacao(item["produto"])
        except Exception as e:
            print(f"{e}: Limite de cota da API atingida. Alterando de agente")
            agents = Agents(client,modelos_fallback[numero_modelo]) 
            numero_modelo += 1
            numero_modelo = numero_modelo % len(modelos_fallback)
            produto = agents.agente_formatacao(item["produto"]) 

        # print(type(dicionario_compras["dados_da_compra"]["date"]))
        data_compra = dicionario_compras["dados_da_compra"]["date"]
        # data_compra = ast.literal_eval(dicionario_compras["dados_da_compra"]["date"])
        # print("string convertida em lista")
        if type(dicionario_compras["dados_da_compra"]["date"]) == list:
            dicionario_compras["dados_da_compra"]["date"]  = datetime(*data_compra, tzinfo=ZoneInfo("America/Sao_Paulo")) #, tzinfo=ZoneInfo("America/Sao_Paulo")) 
        # print("lista convertida em datetime")
        totais =  dicionario_compras["totais"] 
        totais["valor_total"] = converte_float(totais["valor_total"])    
        totais["valor_pago"] = converte_float(totais["valor_pago"])     
        nova_entrada = {
              "id_compra": compra_id,
              "nome_produto": produto["nome_produto"],
              "marca": produto["marca"],
              "categoria": produto["categoria"],              
              "quantidade_produto": produto["quantidade_produto"],
              "unidade_medida_produto": produto["unidade_medida_produto"],
              "quantidade": converte_float(item["quantidade"]),
              "unidade_medida": item["unidade_medida"],
              "valor_unitario": converte_float(item["valor_unitario"]),
              "valor_total_produto": converte_float(item["valor_total_produto"]),
              "valor_desconto_produto": converte_float(item["valor_desconto_produto"]),
              "estabelecimento": dicionario_compras["estabelecimento"],
              "dados_da_compra": dicionario_compras["dados_da_compra"],
              "totais": totais,
              "_created": _created
          }
        nova_compra.append(nova_entrada)
    return nova_compra

def filtrar_dados(consulta: dict, historico_compras: Collection) -> list:
    valor_procurado = consulta["valor_procurado"]
    agregacao = consulta["agregacao"]
    filtros = consulta["filtros"]
    juncao = consulta["juncao"]
    agrupar_por = consulta["agrupar_por"]

    # Filtrando dados
    condicoes = []
    if juncao is None:
        juncao = "$and"

    # vector_query_list = []

    for filtro in filtros:    
        campo = filtro["tipo"]
        comparacao = filtro["comparacao"]
        itens = filtro["itens"]
        itens_formatados = []
        for item in itens:
            try:
                itens_formatados.append(datetime.strptime(item, "%Y-%m-%d"))
            except:
                if campo in ["nome_produto", "marca", "categoria"]:
                    item = item.lower()
                    item = unicodedata.normalize('NFKD', item).encode('ASCII', 'ignore').decode('utf-8')
                    itens_formatados.append(item)
                else:
                    itens_formatados.append(item)                   
        #     vector_query = {
        #         "$vectorSearch": {
        #             "queryVector": converte_embedding(campo),
        #             "path": campo + "_embedding",
        #             "numCandidates": 100,
        #             "limit": 10,
        #             "index": "vector_index"
        #         }
        #     }
        #     vector_query_list.append(vector_query)

        if comparacao == "$in":
            condicoes.append({campo: {comparacao: itens_formatados}})
        else:
            condicoes.append({campo: {comparacao: itens_formatados[0]}})          

    query = {juncao: condicoes}
    print(f"Parâmetros:\n{consulta}", end="\n\n")
    # print(vector_query_list)
    # print(query)
    # resultados = list(historico_compras.find(query, {'_id': 0}))

    pipeline = []

    if agregacao == "$count":
        pipeline.insert(0,{"$count": "retorno"})
    elif agregacao:
        pipeline.insert(0,{"$group": {"_id":  None,"retorno": {agregacao: f"${valor_procurado}"}}})
        # TODO implementar agrupar_por
        # "_id": f"${agrupar_por}" if agrupar_por else None,

        
    if condicoes:
        pipeline.insert(0,{"$match": query})

    # for query_vector in vector_query_list:
    #     pipeline.insert(0, query_vector)
    print(f"Consulta:\n{pipeline}", end="\n\n")
    # busca_vetores = list(historico_compras.aggregate(vector_query_list))
    # for item in busca_vetores:
    #     print(item)
    resultados = list(historico_compras.aggregate(pipeline))
    print(f"Retorno:\n{resultados}", end="\n\n\n")
    return resultados

