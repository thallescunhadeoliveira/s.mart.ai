from prompts import Prompts
from PIL import Image
import google.generativeai as genai
from utils.utils import formata_json


class Agents:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.prompts = Prompts()

    def agente_leitor(self, caminho_arquivo: str) -> str:
        image_path = caminho_arquivo
        try:
            img = Image.open(image_path)
        except FileNotFoundError:
            print(f"Erro: A imagem '{image_path}' não foi encontrada.")
            exit()
        # Ler a imagem em formato de bytes
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        # Exibir a resposta
        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                genai.types.Part.from_bytes(
                data=image_data,
                mime_type='image/jpeg',
                ),
                self.prompts.prompt_imagem
            ]
        )
        response = formata_json(response)
        return response