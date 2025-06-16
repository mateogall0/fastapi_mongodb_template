#!/usr/bin/env python3
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.conn import db
from app.core.config import settings


API_v1_PREFIX = '/v1'

@pytest.fixture
def client():
    client = TestClient(app, f'http://testserver{API_v1_PREFIX}')
    yield client
    db.client.drop_database(settings.DATABASE_NAME)
