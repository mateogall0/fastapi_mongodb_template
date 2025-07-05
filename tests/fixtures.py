import pytest, asyncio, pytest_asyncio
from fastapi.testclient import TestClient
from app.main import app
from app.infra.db import init_db
from app.infra.config import settings
from app.core.models import Base


API_V1_PREFIX = '/v1'

@pytest_asyncio.fixture
async def db():
    db, client_db = await init_db()
    yield db, client_db
    await client_db.drop_database(db.name)

@pytest.fixture
def client(db):
    with TestClient(app, base_url=f"http://testserver{API_V1_PREFIX}") as client:
        yield client
