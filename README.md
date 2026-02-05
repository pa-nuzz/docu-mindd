# Docu-Mind

**Docu-Mind** is a simple web app to upload PDF or DOCX files, extract text (including scanned images via OCR), and clean it for easy use.

---

## Features

- Upload **PDF** or **DOCX** files
- Extract text from documents
- OCR support for scanned PDFs or images
- Clean text output
- Files saved locally in `uploads/`

---

## Installation

**Clone the repository:**

**git clone https://github.com/yourusername/docu-mind.git**

**cd docu-mind**

---

## Creating and activating a virtual environment:
**python -m venv .venv
source .venv/bin/activate**  

## Installing dependencies:
**pip install -r requirements.txt**

---

## Starting the server:
**uvicorn app.main:app --reload**

**Open in browser:
http://127.0.0.1:8000/
Upload your PDF or DOCX file and see the extracted, cleaned text.**
