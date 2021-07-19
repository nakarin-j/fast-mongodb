from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

from schemas.pyobject import PyObjectId

class InputItem(BaseModel):
    name: str
    description: Optional[str] = None


class Item(BaseModel):
    id: PyObjectId = Field(..., alias='_id')
    name: str
    description: Optional[str]


class UpdateItem(BaseModel):
    name: Optional[str]
    description: Optional[str]