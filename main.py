from datetime import datetime
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from routers import events, media
from contextlib import asynccontextmanager
from lib.mongo_connection import connect_mongo, close_mongo

@asynccontextmanager
async def lifespan(my_app:FastAPI):
    await connect_mongo()
    yield
    await close_mongo()

app = FastAPI(lifespan=lifespan)

app.include_router(events.router)
app.include_router(media.router)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}