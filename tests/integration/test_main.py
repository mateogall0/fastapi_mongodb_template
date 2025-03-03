#!/usr/bin/env python3
from tests import client

def test_get(client):
    response = client.get("/")
    assert response.status_code == 200
