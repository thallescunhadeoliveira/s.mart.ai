from pymongo import MongoClient
import os
import sys
# Adiciona o diretório raiz ao sys.path para permitir imports relativos entre pastas
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from app.config import MONGODB_URI

client = MongoClient(MONGODB_URI)

db = client["smartai"]

historico_compras = db["historico_compras"]
