import re

def formalize_sentences(text: str) -> str:
    replacements = {
        r"\bgonna\b": "going to",
        r"\bwanna\b": "want to",
        r"\bgotta\b": "have to",
        r"\betc\.\b": "and so on",
        r"\bASAP\b": "as soon as possible",
        r"\bbtw\b": "by the way",
        r"\bstuff\b": "materials",
        r"\bguy[s]?\b": "team members",
        r"\bpls\b": "please",
        r"\bthx\b": "thank you",
        r"\bokay\b": "okay",
        r"\bngl\b": "not going to lie"
        # Add more if needed
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Fix capitalization after a period (basic version)
    text = re.sub(r'(?<=[.?!])\s+([a-z])', lambda m: f" {m.group(1).upper()}", text)

    return text

def clarify_attributions(text: str) -> str:
    refined_lines = []

    for line in text.split('\n'):
        match = re.match(r"(\w+):\s*(.+)", line)
        if match:
            speaker, statement = match.groups()
            statement = statement.strip().rstrip(".")
            refined = f"{speaker} suggested that \"{statement[0].upper() + statement[1:]}\"."
            refined_lines.append(refined)
        else:
            refined_lines.append(line)

    return '\n'.join(refined_lines)
