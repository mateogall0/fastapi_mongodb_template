from datetime import datetime, timezone
from dataclasses import field
from abc import ABC

class Base(ABC):
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class BaseEmbedded(ABC):
    pass
