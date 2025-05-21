# import os
# from dotenv import load_dotenv
from google import genai

# load_dotenv()

# api_key = os.getenv("GOOGLE_API_KEY")

# client = genai.Client(api_key=api_key)

MODEL_ID = "gemini-2.0-flash"

# MONGODB_URI = os.getenv("MONGODB_URI")

import os
import streamlit as st

# Usa st.secrets no Streamlit Cloud, dotenv localmente
if "API_KEY" in st.secrets:
    os.environ["API_KEY"] = st.secrets["API_KEY"]
    os.environ["MONGO_URI"] = st.secrets["MONGO_URI"]
else:
    from dotenv import load_dotenv
    load_dotenv()

api_key = os.getenv("API_KEY")
MONGODB_URI = os.getenv("MONGO_URI")