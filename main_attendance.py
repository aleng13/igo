from pathlib import Path
from attendance.attendance_extractor import extract_attendance

# Path to your image
image_path = Path("attendance/sample_attendance.jpg")

# Run extraction
attendance = extract_attendance(image_path)

# Display results
print("\n📋 Attendance Extracted:")
for entry in attendance:
    status = "Present ✅" if entry["present"] else "Absent ❌"
    print(f"{entry['name']}: {status}")
