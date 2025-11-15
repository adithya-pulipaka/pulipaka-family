from typing import Optional, Annotated
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from fastapi_camelcase import CamelModel

PyObjectId = Annotated[str, BeforeValidator(str)]
# // {
# //     "type": "file",
# //     "bucket": "fir-poc-bb964.firebasestorage.app",
# //     "generation": "1762922022374496",
# //     "metageneration": "1",
# //     "fullPath": "albums/1/ATTBill_9940_Feb2025.pdf",
# //     "name": "ATTBill_9940_Feb2025.pdf",
# //     "size": 663661,
# //     "timeCreated": "2025-11-12T04:33:42.377Z",
# //     "updated": "2025-11-12T04:33:42.377Z",
# //     "md5Hash": "sEQdEVTEPUJX5qV6eSCz2w==",
# //     "contentDisposition": "inline; filename*=utf-8''ATTBill_9940_Feb2025.pdf",
# //     "contentEncoding": "identity",
# //     "contentType": "application/pdf"
# // }
class Image(CamelModel):
    name: str = None
    bucket: str = None
    size: int = None
    full_path: str = None
    content_type: str = None
    md5_hash: str = None

    model_config = ConfigDict(
        populate_by_name=True,  # Accept both event_id and _id
        arbitrary_types_allowed=True,  # Allow ObjectId type
        json_encoders={ObjectId: str}  # Convert ObjectId to string
    )

