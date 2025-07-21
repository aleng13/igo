# utils/gemini_api.py

import google.generativeai as genai
from utils.auth import get_env_var

genai.configure(api_key=get_env_var("GEMINI_API_KEY"))

def get_model(model_type="pro"):
    if model_type == "flash":
        return genai.GenerativeModel("gemini-1.5-flash")
    # fallback to flash if quota hit
    return genai.GenerativeModel("gemini-1.5-flash")
