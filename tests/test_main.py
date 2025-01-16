#!/usr/bin/env python3
from . import client

def test_get():
    response = client.get("/")
    assert response.status_code == 200
