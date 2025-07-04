from beanie import Document
from app.core.models import *

class BaseDoc(Base, Document): pass
