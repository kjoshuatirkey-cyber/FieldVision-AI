import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_ai(prompt):
    response = model.generate_content(prompt)
    return response.text

def get_ai_response(text: str) -> str:
    """Backward-compatible wrapper used by existing API routes."""
    return ask_ai(text)
