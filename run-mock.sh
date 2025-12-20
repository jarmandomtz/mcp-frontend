source venv3.11/bin/activate

./venv3.11/bin/python3 -m pip install uvicorn fastapi jinja2 google-cloud-bigquery httpx python-dotenv starlette itsdangerous pydantic_settings python-multipart
./venv3.11/bin/python3 -m pip install "passlib[argon2]"

./venv3.11/bin/python3 -m uvicorn mock_ai.server:app --host 0.0.0.0 --port 8002