#text_cleaning.py

import re

def clean_text(raw_text: str) -> str:
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', raw_text)
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()
