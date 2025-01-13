from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar las plantillas
templates = Jinja2Templates(directory="templates")

# Ruta principal que sirve "index.html"
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Otra ruta para la página "hola.html"
@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("hola.html", {"request": request})

# Otra ruta para "students.html"
@app.get("/students", response_class=HTMLResponse)
async def students_page(request: Request):
    return templates.TemplateResponse("students.html", {"request": request})
