from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/personajes", response_class=HTMLResponse)
async def personajes_page(request: Request):
    return templates.TemplateResponse("personajes.html", {"request": request})

@app.get("/transformaciones", response_class=HTMLResponse)
async def transformaciones_page(request: Request):
    return templates.TemplateResponse("transformaciones.html", {"request": request})

@app.get("/esferas", response_class=HTMLResponse)
async def esferas_page(request: Request):
    return templates.TemplateResponse("esferas.html", {"request": request})

from fastapi.responses import FileResponse

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
