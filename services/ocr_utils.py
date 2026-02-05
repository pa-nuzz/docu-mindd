#ocr_utils.py
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_with_ocr(file_bytes: bytes) -> str:
    # Convert PDF to images (or image file) and extract text
    images = convert_from_bytes(file_bytes)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
