import base64
import json  # ✅ ADDED: Import the json library for safe parsing
from pathlib import Path
# Assuming your gemini_api.py is in a 'utils' folder
from utils.gemini_api import generate_with_image

def load_image_base64(image_path):
    """Encodes an image file to a base64 string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def extract_attendance(image_path):
    """
    Extracts attendance data from an image using Gemini,
    with an improved prompt and secure JSON parsing.
    """
    image_base64 = load_image_base64(image_path)
    
    # ✅ UPDATED PROMPT: Made the rule for 'absent' even more explicit.
    prompt = """
    Analyze the provided image of an attendance sheet. Your task is to extract the name from each row and determine if the person was present or absent.

    Follow these rules precisely:
    1.  A person is 'present' (true) ONLY if there is clear, distinct handwriting in the signature box.
    2.  A person is 'absent' (false) if the signature box contains NO handwriting. An empty box or a box with only a pre-printed horizontal line must be considered absent.

    Return ONLY a valid JSON list of objects. Do not use markdown code fences or add explanations.
    """
    
    response = generate_with_image(prompt, image_base64)
    
    # ✅ ADDED: A cleaning step to handle potential markdown code fences from the API.
    # This finds the start of the JSON (the first '{' or '[') and the end (the last '}' or ']')
    # and extracts only the content between them.
    try:
        start = response.find('[')
        end = response.rfind(']') + 1
        if start != -1 and end != 0:
            clean_response = response[start:end]
        else: # Fallback for single object JSON
            start = response.find('{')
            end = response.rfind('}') + 1
            clean_response = response[start:end]

        attendance_data = json.loads(clean_response)
        return attendance_data
    except (json.JSONDecodeError, IndexError) as e:
        print(f"Error: Failed to parse the cleaned JSON. {e}")
        print("--- Raw Response from API ---")
        print(response)
        print("-----------------------------")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Ensure the image path is correct. The original image was a .jpeg
    image_path = Path("attendance/sample_attendance.jpeg")
    
    if not image_path.exists():
        print(f"Error: Image not found at path: {image_path}")
    else:
        attendance = extract_attendance(image_path)
        
        if attendance:
            print("\n📋 Attendance Extracted:")
            for entry in attendance:
                # Ensure the keys exist before accessing them to prevent errors
                name = entry.get("name", "N/A")
                is_present = entry.get("present", False)
                
                status = "Present ✅" if is_present else "Absent ❌"
                print(f"{name}: {status}")
        else:
            print("\nCould not extract attendance data. Please check the error messages above.")