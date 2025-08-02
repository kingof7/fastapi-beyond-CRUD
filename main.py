from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Welcome to the Bookly API!"}

@app.get('/greet/{name}')
async def greet_name(name:str) -> dict:
    return {"message": f"Greetings, {name}!"}