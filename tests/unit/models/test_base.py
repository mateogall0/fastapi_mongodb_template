#!/usr/bin/env python3
from tests import db
from app.core.models import Base
from bson import ObjectId
from datetime import datetime
import pytest


@pytest.mark.asyncio
async def test_basic_attrs(db):
    from app.core.conn import ExampleBase
    ex = ExampleBase(name='test')
    await ex.insert()
    assert isinstance(ex.id, ObjectId)
    assert isinstance(ex.created_at, datetime)
    assert isinstance(ex.updated_at, datetime)
