import os
from dotenv import load_dotenv
from google.generativeai import Client

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = Client(api_key=api_key)

MODEL_ID = "gemini-2.0-flash"

MONGODB_URI = os.getenv("MONGODB_URI")