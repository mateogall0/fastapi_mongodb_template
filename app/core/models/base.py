from beanie import Document, before_event, Insert, Replace, Update
from datetime import datetime, timezone
from pydantic import Field, BaseModel as BaseEmbedded


class Base(Document):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @before_event(Insert)
    def set_created_at(self):
        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now

    @before_event(Update)
    def set_updated_at_on_update(self):
        self.updated_at = datetime.now(timezone.utc)

    @before_event(Replace)
    def set_updated_at(self):
        self.updated_at = datetime.now(timezone.utc)

    class Settings:
        is_root = True 


