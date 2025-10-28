from datetime import datetime
from pydantic import BaseModel,UUID4
import uuid

class Event(BaseModel):
    event_id: UUID4 = None
    event_name: str = None
    event_start_time: datetime = None
    event_end_time: datetime = None
    location: str = None
    description: str = None