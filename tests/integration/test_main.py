from tests import client, db
import pytest

@pytest.mark.asyncio
async def test_get(client):
    response = await client.get("/")
    assert response.status_code == 200
