from datetime import datetime
from typing import Annotated, Optional
from bson import ObjectId

from pydantic import BaseModel, Field, BeforeValidator, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]

class Event(BaseModel):
    event_id: Optional[PyObjectId] = Field(alias="_id", default=None, serialization_alias="event_id")
    event_name: str = None
    event_start_time: datetime = None
    event_end_time: datetime = None
    location: str = None
    description: str = None

    model_config = ConfigDict(
        populate_by_name=True,  # Accept both event_id and _id
        arbitrary_types_allowed=True,  # Allow ObjectId type
        json_encoders={ObjectId: str}  # Convert ObjectId to string
    )