from typing import Optional, Annotated
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class Image(BaseModel):
    name: str = None
    full_path: str = None

    model_config = ConfigDict(
        populate_by_name=True,  # Accept both event_id and _id
        arbitrary_types_allowed=True,  # Allow ObjectId type
        json_encoders={ObjectId: str}  # Convert ObjectId to string
    )

