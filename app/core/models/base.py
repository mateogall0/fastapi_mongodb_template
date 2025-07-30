from datetime import datetime
from abc import ABC
from typing import Any

class Base(ABC):
    id: Any
    created_at: datetime
    updated_at: datetime

class BaseEmbedded(ABC):
    pass
