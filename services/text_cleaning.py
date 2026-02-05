# #text_cleaning.py
#
# import re
#
# def clean_text(raw_text: str) -> str:
#     # Normalize whitespace
#     text = re.sub(r'\s+', ' ', raw_text)
#     # Remove special characters
#     text = re.sub(r'[^\w\s]', '', text)
#     return text.strip()

import re

def clean_text(raw_text: str) -> str:
    """
    Clean text for NLP usage.
    Keeps important symbols like emails and links.
    """

    # remove tabs and line breaks
    text = re.sub(r'[\t\r\n]+', ' ', raw_text)

    # normalize spaces
    text = re.sub(r'\s+', ' ', text)

    # remove unwanted characters but keep useful ones
    text = re.sub(r'[^\w\s@.\-:/]', '', text)

    return text.strip()
