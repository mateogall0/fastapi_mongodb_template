from tests import db
import pytest

@pytest.mark.asyncio
async def test_generic(db):
    from app.repository.base import BaseRepository as BaseService
    class ExampleService(BaseService):
        pass
    from app.core.db_conn import ExampleBase
    service = ExampleService(ExampleBase)
    new = await service.create({'name': 'John Doe'})
    assert new.name == 'John Doe'
    id = new.id

    stored = await service.get(_id=id)
    assert stored.name == 'John Doe'

    date = str(stored.updated_at)

    many = await service.get_many()
    assert len(many) == 1

    updated = await service.update(stored, {'name': "John Doe 2"})
    assert updated.name == "John Doe 2"

    stored = await service.get(_id=id)
    assert stored.name == 'John Doe 2'
    assert str(stored.updated_at) != date


    res = await service.delete_where(_id=id)
    assert res == True

    check_stored = await service.get(_id=id)
    assert check_stored is None
