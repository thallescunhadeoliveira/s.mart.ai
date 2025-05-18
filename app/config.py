import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

MODEL_ID = "gemini-2.0-flash"

MONGODB_URI = os.getenv("MONGODB_URI")