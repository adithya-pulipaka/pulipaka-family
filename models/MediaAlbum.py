from pydantic import BaseModel, BeforeValidator, Field, ConfigDict
from typing import Optional, Annotated, List
from bson import ObjectId
from fastapi_camelcase import CamelModel

from models.Image import Image

PyObjectId = Annotated[str, BeforeValidator(str)]

class MediaAlbum(CamelModel):
    album_id: Optional[PyObjectId] = Field(alias="_id", default=None, serialization_alias="albumId")
    event_id: str = Field(default=None, serialization_alias="eventId")
    images: list[Image] = []

    model_config = ConfigDict(
        populate_by_name=True,  # Accept both event_id and _id
        arbitrary_types_allowed=True,  # Allow ObjectId type
        json_encoders={ObjectId: str}  # Convert ObjectId to string
    )

