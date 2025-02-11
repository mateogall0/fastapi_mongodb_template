#!/usr/bin/env python3
from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.conn import db
from app.config import settings

@pytest.fixture
def client():
    client = TestClient(app)
    yield client
    db.client.drop_database(settings.DATABASE_NAME)
