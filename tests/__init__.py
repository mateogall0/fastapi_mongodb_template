#!/usr/bin/env python3
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
