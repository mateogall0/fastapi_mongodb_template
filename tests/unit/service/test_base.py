from tests import db
from app.service.base import MongoService, SocketRequestService
import pytest


@pytest.mark.asyncio
async def test_crud0(db):
    from app.repository.base import MongoRepository
    class ExampleRepository(MongoRepository):
        pass
    from app.infra.db import ExampleBase
    repo = ExampleRepository(ExampleBase)

    service = MongoService(repo)

    new = await service.create({'name': 'John Doe'})
    assert new.name == 'John Doe'
    id = str(new.id)

    stored = await service.get(id)
    assert stored.name == 'John Doe'

    date = str(stored.updated_at)

    many = await service.search()
    assert len(many) == 1

    updated = await service.update(stored, {'name': "John Doe 2"})
    assert updated.name == "John Doe 2"

    stored = await service.get(id)
    assert stored.name == 'John Doe 2'
    assert str(stored.updated_at) != date

    res = await service.delete(stored)
    assert res == True

    check_stored = await service.get(id)
    assert check_stored is None

@pytest.mark.asyncio
async def test_ws():
    class Example(SocketRequestService):
        async def test_req(self, payload: dict):
            return {'res': payload['num'] * 2}
    sr = Example()

    res = await sr.handshake()
    assert res == {'status': 'connected'}

    res = await sr.handle('test_req', {'num': 5})
    assert res == {'res': 10}

    res = await sr.handle('test_req', {'num': 15})
    assert res == {'res': 30}

    res = await sr.handle('ping', {})
    assert res == {'status': 'pong'}

    res = await sr.handle('unexisting', {})
    assert res == {'error': 'unknown action `unexisting`'}

    res = await sr.handle('handle', {})
    assert res == {'error': 'wrong action type'}
