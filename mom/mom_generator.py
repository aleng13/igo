# mom/mom_generator.py

from utils.gemini_api import get_model

def generate_mom(raw_notes: str) -> str:
    prompt = f"""
You are an expert meeting assistant for a professional student organization.

Your task is to convert the following rough meeting notes into a clean, well-structured, and formal **Minutes of Meeting (MoM)** document.

Please follow the structure below and infer all required details from the content. Create your own relevant **section titles/headings** based on the topics discussed in the meeting — even if the notes are scattered. Group all related points logically and make the flow easy to follow.

--- FORMAT START ---

📄 **MINUTES OF MEETING-<Auto or Manual Numbering>**

**Date**: Extract from notes if available; else write “Not specified”  
**Time**: Extract if possible; else “Not specified”  
**Venue**: Extract if possible; else “Not specified”  
**MOM Number**: CELL/IEDC/2025/ (default)

Write an opening sentence like:  
“A meeting was conducted on <date> at <venue> from <time>. The meeting was presided by <name(s)>.”

**Attendees**:  
(Leave this section blank — do NOT guess names or fill it.)

---

## **Highlights of the Meeting**

- Create **clear and descriptive section titles** based on content
- Group related points together even if they appear scattered
- Use bullet points under each section
- **Mention names** like “John”, “Anwyl”, “Reshma” etc. wherever a person speaks or contributes
- Include task ownership, context, and intent behind the statements

---

### 📅 **Deadlines to be Noted**

Create a table in the following format with any deadline/event/task-related notes found:

| SI No | Events/Occasions/Meetings       | Assigned To     | Sign |
|-------|----------------------------------|------------------|------|
| 1.    |                                  |                  |      |
| 2.    |                                  |                  |      |
...

Use formal language and maintain a professional, clean tone. Keep formatting consistent and readable.

---

Here are the raw notes to format:
{raw_notes}
"""


    model = get_model("pro")
    response = model.generate_content(prompt)
    return response.text
