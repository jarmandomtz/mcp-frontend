# mcp-frontend

MCP front end App

<details close>
<summary>mcp-frontend copilot prompt</summary>

Prompt
I need to create a web application in Python that will serve as the front-end for an AI application. Interaction with the AI ​​application will be via a REST API, to which requests will be sent via POST in the `message` parameter. The application must be responsive and visually appealing, using an orange color scheme. It should have role-based authentication and authorization (admin, user, viewer), initially based on a table in Google Cloud Platform (GCP) BigQuery. The application must be ready for deployment on GCP using a virtual machine and a Terraform script. The Terraform script will also create the necessary resources, such as a service account named `mcp-sre-assistant-sa`. A set of test cases is required. Initially, a mock of the AI ​​application's REST API will also be needed to allow development to proceed while the actual REST API is being created. Class names, variable names, and code documentation must be in English.

copilot prompt: https://copilot.microsoft.com/chats/i8scNkMN7iyAGUAEeJmE2

</details>

<details close>
<summary>mcp-frontend app dir structure</summary>

mcp-sre-assistant/
├─ app/
│  ├─ main.py
│  ├─ auth.py
│  ├─ rbac.py
│  ├─ ai_client.py
│  ├─ bigquery_client.py
│  ├─ settings.py
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ login.html
│  │  ├─ dashboard.html
│  │  ├─ admin.html
│  ├─ static/
│  │  ├─ css/orange.css
│  │  ├─ js/app.js
├─ mock_ai/
│  ├─ server.py
├─ tests/
│  ├─ test_auth.py
│  ├─ test_rbac.py
│  ├─ test_ai_integration.py
├─ terraform/
│  ├─ main.tf
│  ├─ variables.tf
│  ├─ outputs.tf
│  ├─ startup.sh
├─ requirements.txt
├─ README.md

</details>