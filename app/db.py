from config import MONGODB_URI
from pymongo import MongoClient

client = MongoClient(MONGODB_URI)

db = client["smartai"]

historico_compras = db["historico_compras"]
