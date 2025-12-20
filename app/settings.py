# app/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #project_id: str
    project_id: str = "thematic-bee-473421-i7" #"test-project"
    bq_dataset: str = "mcp_sre_assistant"
    bq_users_table: str = "users"
    ai_api_url: str = "http://127.0.0.1:8002/respond"
    #session_secret_key: str
    session_secret_key: str = "test-secret"
    gcp_sa_credentials_json: str | None = None  # path to JSON or None for default creds

settings = Settings()
