import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

def _resolve_model_name() -> str:
    """
    Resolve a working Gemini model name.
    Priority:
    1) GEMINI_MODEL from env
    2) First available model that supports generateContent
    3) A conservative fallback
    """
    env_model = os.getenv("GEMINI_MODEL")
    if env_model:
        return env_model

    try:
        models = genai.list_models()
        for m in models:
            methods = getattr(m, "supported_generation_methods", []) or []
            if "generateContent" in methods:
                # Model names come as "models/<name>"
                return m.name.replace("models/", "")
    except Exception:
        pass

    return "gemini-1.5-flash-latest"

model = genai.GenerativeModel(_resolve_model_name())

def ask_ai(prompt):
    response = model.generate_content(prompt)
    return response.text

def get_ai_response(text: str) -> str:
    """Backward-compatible wrapper used by existing API routes."""
    return ask_ai(text)
