import pytest, asyncio, pytest_asyncio
from app.api.main import app
from app.infra.db import init_db
from app.infra.config import settings
from app.core.models import Base
from httpx import AsyncClient, ASGITransport


API_V1_PREFIX = '/v1'


@pytest_asyncio.fixture
async def db():
    db, client_db = await init_db()
    yield db, client_db
    await client_db.drop_database(db.name)

@pytest_asyncio.fixture
async def client(db):
    transport = ASGITransport(app=app)  # embeds the FastAPI app
    async with AsyncClient(transport=transport, base_url=f"http://testserver{API_V1_PREFIX}") as ac:
        yield ac
