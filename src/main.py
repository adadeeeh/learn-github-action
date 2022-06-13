import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hello")
def hello():
    return {"Hello": "World"}

@app.get("/hi")
def hi():
    return {"Hi": "There"}


if __name__ == "__main__":
    uvicorn.run("main:app")