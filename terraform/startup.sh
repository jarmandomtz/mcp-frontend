# terraform/startup.sh
#!/usr/bin/env bash
set -euxo pipefail

apt-get update
apt-get install -y python3-pip git python3.11-venv tree

# App location
APP_DIR="/opt/mcp-sre-assistant"
mkdir -p "$APP_DIR"
cd "$APP_DIR"

# Pull your repo (replace with your source)
# git clone https://your-repo-url.git .
git clone -b 1.0.0 --single-branch https://github.com/jarmandomtz/mcp-frontend.git .
# For demo, create a venv and install

# Create python virtual environment
#sudo apt install python3.11-venv tree
python3 -m venv venv
source venv/bin/activate

# Install python packages
/opt/mcp-sre-assistant/venv/bin/python3 -m pip install --upgrade pip
/opt/mcp-sre-assistant/venv/bin/python3 -m pip install uvicorn fastapi jinja2 passlib[argon2] google-cloud-bigquery httpx python-dotenv starlette itsdangerous pydantic_settings

export MYSECRET="$(openssl rand -hex 32)"

cat > /etc/systemd/system/mcp.service <<'UNIT'
[Unit]
Description=MCP SRE Assistant
After=network.target

[Service]
Type=simple
Environment=SESSION_SECRET_KEY=${MYSECRET}
Environment=PROJECT_ID=${PROJECT_ID}
WorkingDirectory=/opt/mcp-sre-assistant
ExecStart=/opt/mcp-sre-assistant/venv/bin/python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
UNIT

systemctl daemon-reload
systemctl enable mcp.service
systemctl start mcp.service

# Mock server for development
cat > /etc/systemd/system/mock-ai.service <<'UNIT'
[Unit]
Description=Mock AI Server
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/mcp-sre-assistant
ExecStart=/opt/mcp-sre-assistant/venv/bin/python3 -m uvicorn mock_ai.server:app --host 0.0.0.0 --port 8002
Restart=always

[Install]
WantedBy=multi-user.target
UNIT

systemctl daemon-reload
systemctl enable mock-ai.service
systemctl start mock-ai.service
