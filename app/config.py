import os
import toml
from dotenv import load_dotenv

# Inicializa variáveis
api_key = None
MONGODB_URI = None

# 1. Tenta buscar via streamlit.secrets (se estiver rodando dentro do Streamlit)
try:
    import streamlit as st
    api_key = st.secrets["google_api"]["key"]
    MONGODB_URI = st.secrets["mongodb"]["string"]
except Exception:
    pass  # Se não estiver no Streamlit, tenta os outros métodos

# 2. Tenta via secrets.toml local (para desenvolvimento local)
if not api_key or not MONGODB_URI:
    try:
        secrets = toml.load("secrets.toml")
        api_key = api_key or secrets["google_api"]["key"]
        MONGODB_URI = MONGODB_URI or secrets["mongodb"]["string"]
    except Exception:
        pass

# 3. Fallback final para variáveis de ambiente (.env)
if not api_key or not MONGODB_URI:
    load_dotenv()
    api_key = api_key or os.getenv("GOOGLE_API_KEY")
    MONGODB_URI = MONGODB_URI or os.getenv("MONGODB_URI")

# Validação (opcional)
if not api_key:
    raise ValueError("API Key do Google Gemini não encontrada.")
if not MONGODB_URI:
    raise ValueError("String de conexão com MongoDB não encontrada.")

# Agora você pode usar as variáveis
from google import genai
client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.0-flash"




