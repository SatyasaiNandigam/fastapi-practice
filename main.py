from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return  {"response" : "Home"}

@app.get("/cart")
async def get_cart():
    return {"response": "carts here"}