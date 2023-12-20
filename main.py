import httpx as httpx
from fastapi import FastAPI, Request,HTTPException
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    backend = "http://mn-developer.com:1234"
    backend = "http://127.0.0.1:8000"
    variables = {"backend": backend}
    return templates.TemplateResponse("index.html", {"request": request, **variables})


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

