import json
from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv


load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
# Conexão com o MongoDB Atlas
client = MongoClient(MONGODB_URI)
db = client["smartai"]
colecao = db["historico_compras"]

# Ler o arquivo JSON
with open('samples.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)  # dados será uma lista de dicionários

for item in dados:
    item["_created"] = datetime.now(timezone.utc)


# Inserir os dados na coleção
resultado = colecao.insert_many(dados)

print(f"{len(resultado.inserted_ids)} documentos inseridos.")
