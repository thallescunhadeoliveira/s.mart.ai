import json
import time
from PIL import Image
from app.config import client, MODEL_ID, MODEL_ID_LITE, MODEL_ID_15
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import ast


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
        print(image_file)
        image_data = image_file.read()
    
    return image_data


def formata_json(texto: str) -> str:
    texto_ajustado = texto.split("```json\n")[1]
    texto_ajustado = texto_ajustado.split("\n```")[0]
    texto_dict = json.loads(texto_ajustado)
    return texto_dict


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
        print(f"Item{i}: {item}")
        i  += 1
        try:
            produto = agents.agente_formatacao(item["produto"])
        except Exception as e:
            print(f"{e}: Limite de cota da API atingida. Alterando de agente")
            agents = Agents(client,modelos_fallback[numero_modelo]) 
            numero_modelo += 1
            produto = agents.agente_formatacao(item["produto"]) 

        print(type(dicionario_compras["dados_da_compra"]["date"]))
        data_compra = dicionario_compras["dados_da_compra"]["date"]
        # data_compra = ast.literal_eval(dicionario_compras["dados_da_compra"]["date"])
        # print("string convertida em lista")
        if type(dicionario_compras["dados_da_compra"]["date"]) == list:
            dicionario_compras["dados_da_compra"]["date"]  = datetime(*data_compra, tzinfo=ZoneInfo("America/Sao_Paulo")) #, tzinfo=ZoneInfo("America/Sao_Paulo")) 
        print("lista convertida em datetime")         
        nova_entrada = {
              "id_compra": compra_id,
              "nome_produto": produto["nome_produto"],
              "marca": produto["marca"],
              "categoria": produto["categoria"],
              "quantidade_produto": produto["quantidade_produto"],
              "unidade_medida_produto": produto["unidade_medida_produto"],
              "quantidade": item["quantidade"],
              "unidade_medida": item["unidade_medida"],
              "valor_unitario": item["valor_unitario"],
              "valor_total_produto": item["valor_total_produto"],
              "valor_desconto_produto": item["valor_desconto_produto"],
              "estabelecimento": dicionario_compras["estabelecimento"],
              "dados_da_compra": dicionario_compras["dados_da_compra"],
              "totais": dicionario_compras["totais"],
              "_created": _created
          }
        nova_compra.append(nova_entrada)
    return nova_compra