import json
import time
from PIL import Image
from models.agents import Agents
from app.config import client, MODEL_ID


def construir_historico(chat_history, user_input):
    historico_mensagem = ""
    for speaker, message in chat_history[-6:]:  # últimas 6 mensagens, para não crescer demais
        if speaker == "Você":
            prompt += f"Usuário: {message}\n"
        else:
            prompt += f"s.mart.at: {message}\n"
    prompt += f"Usuário: {user_input}\n"
    prompt += "s.mart.at: "
    return historico_mensagem


def pegar_arquivo(image_path: str):

    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Erro: A imagem '{image_path}' não foi encontrada.")
        exit()

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    return image_data


def formata_json(texto: str) -> str:
  texto_ajustado = texto.split("```json\n")[1]
  texto_ajustado = texto_ajustado.split("\n```")[0]
  texto_dict = json.loads(texto_ajustado)
  return texto_dict


def formata_registro(dicionario_compras: dict) -> list:
    #criar função par definir id
    compra_id = str(int(time.time()*1000000))
    agents = Agents(client,MODEL_ID)
    nova_compra = []
    for item in dicionario_compras['itens_comprados']:
        produto = agents.agente_formatacao(item["produto"])
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
          }
        nova_compra.append(nova_entrada)
    return nova_compra