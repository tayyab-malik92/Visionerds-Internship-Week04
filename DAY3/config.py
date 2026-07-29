from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

BASE_URL = "https://api.groq.com/openai/v1"

MODEL = "llama-3.3-70b-versatile"