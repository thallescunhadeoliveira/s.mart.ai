import json
import os
import sys
from google.genai import types
from PIL import Image
from datetime import datetime, timezone
import unicodedata

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from utils.utils import formata_json, filtrar_dados
from models.prompts import Prompts


class Agents:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.prompts = Prompts()

    def agente_leitor(self, image_data: Image.Image) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=[self.prompts.prompt_leitor, image_data]
        )
        descricao_imagem = formata_json(response.text)
        return descricao_imagem
    

    def agente_formatacao(self, item: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_formatador + "\nProduto: " + item,
            config={"tools": [{"google_search": {}}]}
        )
        produto = formata_json(response.text)
        try:
            produto["nome_produto"] = unicodedata.normalize('NFKD', produto["nome_produto"]).encode('ASCII', 'ignore').decode('utf-8').lower()
        except:
            produto["nome_produto"] = None
        try:
            produto["marca"] = unicodedata.normalize('NFKD', produto["marca"]).encode('ASCII', 'ignore').decode('utf-8').lower()
        except:
            produto["marca"] = None
        try:
            produto["categoria"] = unicodedata.normalize('NFKD', produto["categoria"]).encode('ASCII', 'ignore').decode('utf-8').lower()
        except:
            produto["categoria"] = None
        
        return produto
    

    def agente_feedback(self, itens: list) -> str:
        for item in itens:
            if '_id' in item:
                item['_id'] = str(item['_id'])
            if '_created' in item:
                item['_created'] = str(item['_created'])
            if item["dados_da_compra"]['date']:
                item["dados_da_compra"]['date'] = str(item["dados_da_compra"]['date'])
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_feedback + "\nProdutos: " + json.dumps(itens),
        )
        return response.text
    

    def agente_buscador(self, pergunta: str, dados: dict) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_buscador + "\nPergunta: " + pergunta,
            config={"tools": [{"google_search": {}}]}
        )
        consulta = formata_json(response.text)
        dados_filtrados = filtrar_dados(consulta, dados)
        return dados_filtrados


    def agente_analista(self, base_dados: list, pergunta: str) -> str:
        for item in base_dados:
            if '_id' in item:
                item['_id'] = str(item['_id'])
            if 'retorno' in item:
                item['retorno'] = str(item['retorno'])
            if '_created' in item:
                item['_created'] = str(item['_created'])
            try:
                item["dados_da_compra"]['date'] = str(item["dados_da_compra"]['date'])
            except:
                pass
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_analista + "\nPergunta usuário: " + pergunta + "\nRetorno da Consulta: " + json.dumps(base_dados)
        )
        analise = response.text
        return analise
    

    def agente_comunicador(self, analise: str, pergunta: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_comunicador + "\nPergunta Usuário: " + pergunta + "\nAnálise de Dados: " + analise
        )
        comunicacao = response.text
        return comunicacao
    

    def agente_conversador(self, mensagem: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_conversador + "\nMensagem Usuário: " + mensagem
        )
        conversa = response.text
        return conversa
    

    def agente_orquestrador(self, mensagem: str):
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_orquestrador + "\nMensagem Usuário: " + mensagem
        )
        agente = response.text
        return agente
    
    def agente_embedding(self, texto: str, tipo: str) -> list:
        response = self.client.models.embed_content(
            model = self.model,
            contents = texto,
            config = types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
        )

        return response.embeddings[0].values
