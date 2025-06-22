import json
import os
import sys
from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from samples import produtos
import unicodedata

# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from utils.utils import converte_embedding


load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
# Conexão com o MongoDB Atlas
client = MongoClient(MONGODB_URI)
db = client["smartai"]
colecao = db["historico_compras"]

for item in produtos:
    item["_created"] = datetime.now(timezone.utc)
    item["nome_produto"] = unicodedata.normalize('NFKD', item["nome_produto"]).encode('ASCII', 'ignore').decode('utf-8').lower()
    item["marca"] = unicodedata.normalize('NFKD', item["marca"]).encode('ASCII', 'ignore').decode('utf-8').lower()
    item["categoria"] = unicodedata.normalize('NFKD', item["categoria"]).encode('ASCII', 'ignore').decode('utf-8').lower()

# Inserir os dados na coleção
resultado = colecao.insert_many(produtos)

print(f"{len(resultado.inserted_ids)} documentos inseridos.")
