from tests import db
from app.core.usecases.crud import CRUDService as MongoService
import pytest


@pytest.mark.asyncio
async def test_crud0(db):
    from app.infra.repository.base import MongoRepository
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

    updated = await service.update(stored, {'name': "John Doe 2"})
    assert updated.name == "John Doe 2"

    stored = await service.get(id)
    assert stored.name == 'John Doe 2'
    assert str(stored.updated_at) != date

    res = await service.delete(stored)
    assert res == True

    check_stored = await service.get(id)
    assert check_stored is None

