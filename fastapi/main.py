from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import asyncio

app = FastAPI()

items = [{"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}]

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def read_items(start: int = 0, limit: int = 10):
    filtered_items = items[start : start + limit]
    return filtered_items

@app.post("/items/")
def create_item(item: Item):
    req = {"name": item.name, "description": item.description, "price": item.price}
    return req

@app.get("/sleep_time/")
async def read_sleep_time(sleep_time: int = 1):
    await asyncio.sleep(sleep_time)
    return {"sleep_time": sleep_time}