
"""
When imported, this module will initialize the mongoengine connectino to
MongoDB using the desired URI
"""
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from beanie import init_beanie
from app.utils import TEST
from .models import *


used_models=[]

if TEST:
    from app.infra.models import BaseDoc

    class ExampleBase(BaseDoc):
        name: str
        class Settings:
            name = "example"
    used_models.append(ExampleBase)


async def init_db(models=used_models):
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client.get_default_database()
    
    await init_beanie(database=db, document_models=models)
    return db, client
