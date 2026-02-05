#main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.pdf_routes import router  # import your PDF/DOCX router

app = FastAPI(title="Docu-Mind API")

# Include the router
app.include_router(router)

# Templates folder
templates = Jinja2Templates(directory="templates")

# Serve uploaded files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Show upload form
    return templates.TemplateResponse("index.html", {"request": request})

