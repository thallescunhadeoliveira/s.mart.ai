import json
import time
from models.agents import Agents
from app.config import client, MODEL_ID

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