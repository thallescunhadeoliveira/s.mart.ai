from google import genai
import toml
import os
from dotenv import load_dotenv

# Tenta buscar via Secrets
try:
    secrets = toml.load("secrets.toml")
    api_key = secrets["google_api"]["key"]
    MONGODB_URI = secrets["mongodb"]["string"]

# Se não for suportado, usa .env
except:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    MONGODB_URI = os.getenv("MONGODB_URI")

client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.0-flash"



