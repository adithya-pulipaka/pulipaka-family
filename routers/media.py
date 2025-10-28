from fastapi import APIRouter, Depends
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.asynchronous.collection import AsyncCollection
from lib.mongo_connection import get_mongo_db
from models.Image import Image
from models.MediaAlbum import MediaAlbum
from bson import ObjectId
from typing import List
import json

router = APIRouter(prefix="/albums")

MEDIA_ALBUM_COLLECTION = "media_album"

def get_album_collection(db: AsyncDatabase) -> AsyncCollection:
    return db.get_collection(MEDIA_ALBUM_COLLECTION)

@router.post("/")
async def create_album(event_id: str, db: AsyncDatabase = Depends(get_mongo_db)) -> MediaAlbum | None:
    coll: AsyncCollection = get_album_collection(db)
    album: MediaAlbum = MediaAlbum(event_id=event_id)
    album_db = album.model_dump(by_alias=True, exclude={"album_id"})
    await coll.insert_one(album_db)
    return album_db

@router.put('/')
async def update_album_with_images(album_id: str, album: MediaAlbum, db: AsyncDatabase = Depends(get_mongo_db)) -> MediaAlbum | None:
    coll: AsyncCollection = get_album_collection(db)
    album_data = await coll.find_one({"_id": ObjectId(album_id)})
    current_album = MediaAlbum(**album_data)
    if current_album.images:
        curr_list: list[Image] = current_album.images
        curr_list.extend(album.images)
        current_album.images = curr_list
        curr_list = [img.model_dump() for img in curr_list]
    else:
        current_album.images = album.images
        curr_list = [img.model_dump() for img in album.images]
    await coll.update_one({"_id":ObjectId(album_id)}, {"$set": {"images":curr_list}})
    return current_album