import pytest, asyncio, pytest_asyncio
from fastapi.testclient import TestClient
from app.main import app
from app.core.db_conn import init_db
from app.core.config import settings
from app.core.models import Base


API_V1_PREFIX = '/v1'

@pytest_asyncio.fixture
async def db():
    db, client_db = await init_db()
    yield db, client_db
    await client_db.drop_database(db.name)

@pytest.fixture
def client(db):
    client = TestClient(app, base_url=f'http://testserver{API_V1_PREFIX}')
    yield client
