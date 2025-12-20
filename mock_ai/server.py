# mock_ai/server.py
from fastapi import FastAPI
from pydantic_settings import BaseModel

app = FastAPI(title="Mock AI Server")

class Msg(BaseModel):
    message: str

@app.post("/respond")
def respond(payload: Msg):
    reply = f"Echo: {payload.message[:200]}"
    return {"reply": reply, "meta": {"model": "mock", "latency_ms": 12}}
