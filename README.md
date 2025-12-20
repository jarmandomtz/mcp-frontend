# mcp-frontend

MCP front end App

<details close>
<summary>mcp-frontend copilot prompt</summary>

Prompt
I need to create a web application in Python that will serve as the front-end for an AI application. Interaction with the AI ​​application will be via a REST API, to which requests will be sent via POST in the `message` parameter. The application must be responsive and visually appealing, using an orange color scheme. It should have role-based authentication and authorization (admin, user, viewer), initially based on a table in Google Cloud Platform (GCP) BigQuery. The application must be ready for deployment on GCP using a virtual machine and a Terraform script. The Terraform script will also create the necessary resources, such as a service account named `mcp-sre-assistant-sa`. A set of test cases is required. Initially, a mock of the AI ​​application's REST API will also be needed to allow development to proceed while the actual REST API is being created. Class names, variable names, and code documentation must be in English.

Copilot prompt: https://copilot.microsoft.com/chats/i8scNkMN7iyAGUAEeJmE2

</details>

<details close>
<summary>mcp-frontend app dir structure</summary>

mcp-sre-assistant/
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── ai_client.py
│   ├── auth.py
│   ├── bigquery_client.py
│   ├── main.py
│   ├── rbac.py
│   ├── settings.py
│   ├── static
│   └── templates
├── mcp_frontend.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
├── mock_ai
│   ├── __pycache__
│   └── server.py
├── pyproject.toml
├── requirements.txt
├── sql
│   └── users.sql
├── terraform
│   ├── README.md
│   ├── main.tf
│   ├── outputs.tf
│   ├── startup.sh
│   ├── startup.sh.bkp
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
├── tests
│   ├── __pycache__
│   ├── test_ai_integration.py
│   ├── test_auth.py
│   └── test_rbac.py
└── venv3.11
    ├── bin
    ├── etc
    ├── include
    ├── lib
    ├── pyvenv.cfg
    └── share

</details>

## Run

<details close>
<summary>Run App</summary>

```shell
# python 3.11
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 -m venv venv3.11
source venv3.11/bin/activate

# Create venv
which pip
./venv3.11/bin/python3 -m pip install uvicorn fastapi jinja2 google-cloud-bigquery httpx python-dotenv starlette itsdangerous pydantic_settings python-multipart
./venv3.11/bin/python3 -m pip install "passlib[argon2]"
# Create app as a package
# Add packages = ["app"] in pyproject.toml
pip install -e .

# Run
which python
./venv3.11/bin/python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

</details>

<details close>
<summary>Run tests</summary>

```shell
# python 3.11
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 -m venv venv3.11
source venv3.11/bin/activate

# Create venv
which python
pip install ipympl ipython jupyterlab matplotlib nodejs numpy seaborn starlette fastapi pytest itsdangerous pydantic_settings passlib google-cloud-bigquery python-multipart
#uvicorn jinja2 passlib[argon2] httpx python-dotenv 
# Create app as a package
which pip
# Add packages = ["app"] in pyproject.toml
pip install -e .

# Run
which pytest
pytest -q
```

</details>