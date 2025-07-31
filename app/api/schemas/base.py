from pydantic import BaseModel, Field, ConfigDict, field_serializer
from datetime import datetime
from bson import ObjectId

class BaseInput(BaseModel):
    pass

class BaseResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes = True,
        arbitrary_types_allowed = True,
        populate_by_name = True,
    )


class ModelResponse(BaseResponse):
    id: ObjectId | str = Field(default_factory=ObjectId, alias='_id')
    created_at: datetime
    updated_at: datetime
    @field_serializer('id')
    def serialize_objectid(self, value: ObjectId) -> str:
        if isinstance(value, ObjectId):
            return str(value)
        return value

class SearchQuery(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(64, ge=1, le=100)
