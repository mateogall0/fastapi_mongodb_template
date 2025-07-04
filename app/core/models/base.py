from datetime import datetime, timezone
from pydantic import Field, BaseModel as BaseEmbedded


class Base(BaseEmbedded):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        is_root = True 

