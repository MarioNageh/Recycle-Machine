import httpx as httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
backend = "https://www.mn-developer.com:8010"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    title = "CanBank.app"
    variables = {"backend": backend, 'title': title}
    return templates.TemplateResponse("landing.html", {"request": request, **variables})



@app.get("/home", response_class=HTMLResponse)
async def read_root(request: Request):
    title = "CanBank.app"
    variables = {"backend": backend, 'title': title}
    return templates.TemplateResponse("index.html", {"request": request, **variables})


@app.get("/help", response_class=HTMLResponse)
async def help(request: Request):
    title = "CanBank.app"
    variables = {"backend": backend, 'title': title}
    return templates.TemplateResponse("help.html", {"request": request, **variables})



@app.get("/menu", response_class=HTMLResponse)
async def help(request: Request):
    title = "CanBank.app"
    variables = {"backend": backend, 'title': title}
    return templates.TemplateResponse("menu.html", {"request": request, **variables})


@app.get("/check/{phone}")
async def check(phone: str):
    print(phone)
    url = f'http://18.218.21.4:8383/api/v1/users/{phone}/useraccount'
    print(url)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400,
                            detail=f"Failed to fetch data. Status code: {response.status_code}")
