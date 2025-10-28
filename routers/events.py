from fastapi import APIRouter
from models.Event import Event
import uuid
from lib.mongo_connection import db

router = APIRouter(prefix='/events')

# dummy data structure for testing
events = []

@router.post("/")
async def create_event(event: Event) -> Event | None:
    modified_event = event.model_dump()
    modified_event["event_id"] = uuid.uuid4()
    events.append(modified_event)
    return modified_event

@router.get("/")
async def get_events() -> list[Event] | None:
    print(db)
    return events