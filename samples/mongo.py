import json
from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from samples import produtos


load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
# Conexão com o MongoDB Atlas
client = MongoClient(MONGODB_URI)
db = client["smartai"]
colecao = db["historico_compras"]

for item in produtos:
    item["_created"] = datetime.now(timezone.utc)

# Inserir os dados na coleção
resultado = colecao.insert_many(produtos)

print(f"{len(resultado.inserted_ids)} documentos inseridos.")
