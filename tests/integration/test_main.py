from tests import client, db
import pytest

def test_get(client):
    response = client.get("/")
    assert response.status_code == 200
