import google.generativeai as genai
from utils.auth import get_env_var
import base64
from PIL import Image
import io

# Configure Gemini API
genai.configure(api_key=get_env_var("GEMINI_API_KEY"))

def get_model(model_type="flash"):
    if model_type == "pro_vision":
        return genai.GenerativeModel("gemini-1.5-pro-vision-latest")
    return genai.GenerativeModel("gemini-1.5-flash")  # Default is flash

def generate_with_image(prompt, image_base64, model_type="flash"):
    model = get_model(model_type)

    try:
        # Decode base64 to image bytes
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))

        response = model.generate_content(
            [prompt, image],
            stream=False,
        )
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"
