# attendance/attendance_extractor.py

import base64
from pathlib import Path
from utils.gemini_api import generate_with_image

def load_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def extract_attendance(image_path):
    image_base64 = load_image_base64(image_path)
    
    prompt = """
    This is a scanned attendance sheet. Extract all printed names. 
    For each name, mark whether a signature is present next to it.
    Return the result as a JSON list with this format:

    [
        {"name": "Alen George", "present": true},
        {"name": "Abraham Manoj", "present": false}
    ]
    """
    
    response = generate_with_image(prompt, image_base64)
    
    try:
        # Gemini returns a stringified JSON, so eval or parse
        attendance_data = eval(response)  # safer if you use `json.loads()` and validate
        return attendance_data
    except Exception as e:
        print("Failed to parse Gemini response:", e)
        print("Raw response:", response)
        return []

if __name__ == "__main__":
    image_path = Path("attendance/sample_attendance.jpg")
    attendance = extract_attendance(image_path)
    
    print("\n📋 Attendance Extracted:")
    for entry in attendance:
        status = "Present ✅" if entry["present"] else "Absent ❌"
        print(f"{entry['name']}: {status}")
