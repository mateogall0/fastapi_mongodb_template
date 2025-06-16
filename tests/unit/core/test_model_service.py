#!/usr/bin/env python3
from tests import client
import pytest

@pytest.mark.asyncio
async def test_generic(client):
    from mongoengine import StringField
    from app.repository.base import BaseRepository as BaseService
    from app.core.models.base import Base
    class ExampleBase(Base):
        name = StringField(required=True)
    class ExampleService(BaseService):
        pass
    service = ExampleService(ExampleBase)
    new = service.create({'name': 'John Doe'})
    assert new.name == 'John Doe'
    id = new.id

    stored = service.get(id=str(id))
    assert stored.name == 'John Doe'

    updated = service.update(stored, {'name': "John Doe 2"})
    assert updated.name == "John Doe 2"

    res = service.delete_where(id=str(id))
    assert res == True

    check_stored = service.get(id=str(id))
    assert check_stored is None

