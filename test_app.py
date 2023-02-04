from app import app
import pytest
import json
#from flask import current_app

@pytest.fixture
def client():
    return app.test_client()


def test_test_connection(client):
    resp = client.get('/ping/Arijit')
    print(resp.json)
    assert resp.status_code == 200
    assert resp.data == b"Welcome Mr. Arijit !"


def test_test_connection_json(client):
    resp = client.get('/ping_json/Arijit')
    print(resp.json)
    assert resp.status_code == 200
    assert resp.json == {"message":"Welcome Mr. Arijit !"}