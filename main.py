from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for POST request
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True


# 1. Root API
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI app 🚀"}


# 2. Path parameter API
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "message": "Item fetched successfully"}


# 3. Query parameter API
@app.get("/search/")
def search_item(q: str = None):
    return {"query": q}


# 4. POST API
@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "availability": item.is_available,
        "message": "Item created successfully"
    }

