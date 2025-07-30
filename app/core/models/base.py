from datetime import datetime
from abc import ABC

class Base(ABC):
    created_at: datetime
    updated_at: datetime

class BaseEmbedded(ABC):
    pass
