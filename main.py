from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    # Replace 'path/to/index.html' with the actual path to your index.html file
    return FileResponse("static/index.html")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
