from beanie import Document
from app.core.models import Base

class BaseDoc(Base, Document):
    pass
