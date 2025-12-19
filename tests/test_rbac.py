# tests/test_rbac.py
from starlette.testclient import TestClient
from app.main import app

def test_forbid_without_login():
    c = TestClient(app)
    r = c.get("/admin")
    assert r.status_code == 401
