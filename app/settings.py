# app/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    project_id: str
    bq_dataset: str = "mcp_sre_assistant"
    bq_users_table: str = "users"
    ai_api_url: str = "http://127.0.0.1:8001/respond"
    session_secret_key: str
    gcp_sa_credentials_json: str | None = None  # path to JSON or None for default creds

settings = Settings()
