from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return  "My home"

@app.get("/cart")
async def get_cart():
    return {"response": "carts here"}