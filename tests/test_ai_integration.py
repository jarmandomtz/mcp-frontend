# tests/test_ai_integration.py
from starlette.testclient import TestClient
from app.main import app

def test_chat_requires_auth():
    c = TestClient(app)
    r = c.post("/chat", data={"message": "hello"})
    assert r.status_code == 401
