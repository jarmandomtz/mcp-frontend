# app/ai_client.py
import httpx
from app.settings import settings

async def send_message_to_ai(message: str) -> dict:
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.post(settings.ai_api_url, json={"message": message})
        r.raise_for_status()
        return r.json()
