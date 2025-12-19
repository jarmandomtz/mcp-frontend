# tests/test_auth.py
import pytest
from starlette.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_login_page(client):
    r = client.get("/login")
    assert r.status_code == 200

def test_login_fail(client, monkeypatch):
    # Stub BigQuery response to None
    from app import bigquery_client
    monkeypatch.setattr(bigquery_client, "fetch_user", lambda email: None)
    r = client.post("/login", data={"email":"x@y.com","password":"bad"})
    assert r.status_code == 401
