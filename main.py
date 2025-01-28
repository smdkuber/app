# main.py
from azure.functions import AsgiMiddleware
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/hello")
async def root2():
    return {"message1": "Hello, World!2"}


@app.get("/welcome")
async def root2():
    return {"message3": "welcome"}

def main(req):
    return AsgiMiddleware(app)

