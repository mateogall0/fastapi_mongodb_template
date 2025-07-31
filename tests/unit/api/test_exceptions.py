from tests import client, db, app, API_V1_PREFIX
from app.core.exceptions import Conflict
import pytest

@pytest.mark.asyncio
async def test_exceptions0(client):
    async def exception0():
        raise Conflict()

    app.router.add_api_route(API_V1_PREFIX + "/exception0",
                             exception0, methods=["GET"], status_code=200)

    res = await client.get('/exception0')
    assert res.status_code == 409

@pytest.mark.asyncio
async def test_exceptions1(client):
    async def exception1():
        raise ValueError()

    app.router.add_api_route(API_V1_PREFIX + "/exception1",
                             exception1, methods=["GET"], status_code=200)

    with pytest.raises(ValueError):
        res = await client.get('/exception1')
