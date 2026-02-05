from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.pdf_routes import router

app = FastAPI(title="Docu-Mind API")

# include upload routes
app.include_router(router)

# templates folder
templates = Jinja2Templates(directory="templates")

# serve uploaded files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
