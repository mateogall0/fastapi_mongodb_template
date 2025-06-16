#!/usr/bin/env python3
from tests import client
from app.core.models import Base
from bson import ObjectId
from datetime import datetime

def test_basic_attrs(client):
    class Example(Base):
        pass

    ex = Example()
    ex.save()
    assert isinstance(ex.id, ObjectId)
    assert isinstance(ex.created_at, datetime)
    assert isinstance(ex.updated_at, datetime)
