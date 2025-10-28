from fastapi import APIRouter, Depends
from models.Event import Event
from lib.mongo_connection import get_mongo_db
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.asynchronous.collection import AsyncCollection

router = APIRouter(prefix='/events')

EVENTS_COLLECTION = "events"

def get_events_collection(db: AsyncDatabase) -> AsyncCollection:
    return db.get_collection(EVENTS_COLLECTION)

@router.post("/")
async def create_event(event: Event, db: AsyncDatabase = Depends(get_mongo_db)) -> Event | None:
    coll: AsyncCollection = get_events_collection(db)
    modified_event = event.model_dump(by_alias=True, exclude={"event_id"})
    await coll.insert_one(modified_event)
    return Event(**modified_event)

@router.get("/")
async def get_events(db: AsyncDatabase = Depends(get_mongo_db)) -> list[Event] | None:
    coll: AsyncCollection = get_events_collection(db)
    events = await coll.find({}).to_list()
    return events