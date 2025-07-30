from beanie import Document
from datetime import datetime, timezone
from app.core.models import Base
from pydantic import Field

class BaseDoc(Base, Document):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
