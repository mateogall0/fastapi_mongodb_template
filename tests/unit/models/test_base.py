from tests import db
from app.core.models import Base
from bson import ObjectId
from datetime import datetime
import pytest


@pytest.mark.asyncio
async def test_basic_attrs(db):
    from app.infra.db import ExampleBase
    ex = ExampleBase(name='test')
    await ex.insert()
    assert isinstance(ex.id, ObjectId)
    assert isinstance(ex.created_at, datetime)
    assert isinstance(ex.updated_at, datetime)
    assert hasattr(ex, 'json')
    assert hasattr(ex, 'dict')
