import google.generativeai as genai
import json
import os
import sys
from google.genai import types

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from utils.utils import formata_json, pegar_arquivo
from models.prompts import Prompts


class Agents:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.prompts = Prompts()

    def agente_leitor(self,caminho_arquivo: str) -> str:
        image_data = pegar_arquivo(caminho_arquivo)
        # Exibir a resposta
        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                types.Part.from_bytes(
                data=image_data,
                mime_type='image/jpeg',
                ),
                self.prompts.prompt_leitor
            ]
        )
        response = formata_json(response)
        return response
    

    def agente_formatacao(self, item: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_formatador + "\nProduto: " + item,
            config={"tools": [{"google_search": {}}]}
        )
        produto = formata_json(response.text)
        return produto
    

    def agente_buscador(self, pergunta: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_buscador + "\nPergunta: " + pergunta,
            config={"tools": [{"google_search": {}}]}
        )
        consulta = formata_json(response.text)
        return consulta


    def agente_analista(self, base_dados: list, pergunta: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=self.prompts.prompt_analista + "\nPergunta usuário: " + pergunta + "\nHistórico de Compras: " + json.dumps(base_dados)
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