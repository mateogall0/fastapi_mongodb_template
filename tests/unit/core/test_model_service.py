#!/usr/bin/env python3
from tests import client
import pytest

@pytest.mark.asyncio
async def test_generic(client):
    from mongoengine import StringField
    from app.core.model_service import BaseService
    from app.models.base import Base
    class ExampleBase(Base):
        name = StringField(required=True)
    class ExampleService(BaseService):
        model = ExampleBase
    service = ExampleService()
    new = service.create({'name': 'John Doe'})
    assert new.name == 'John Doe'
    id = new.id

    stored = service.get(id=str(id))
    assert stored.name == 'John Doe'

    res = service.delete(id=str(id))
    assert res == True

    check_stored = service.get(id=str(id))
    assert check_stored is None
