# create_user.py
from passlib.hash import argon2
from google.cloud import bigquery
from datetime import datetime

PROJECT_ID = "thematic-bee-473421-i7"
DATASET = "mcp_sre_assistant"
TABLE = "users"

email = input("Email: ")
password = input("Password: ")
role = input("Role (admin/user/viewer): ")

hash_value = argon2.hash(password)

client = bigquery.Client(project=PROJECT_ID)

query = f"""
INSERT INTO `{PROJECT_ID}.{DATASET}.{TABLE}`
(email, password_hash, role, created_at)
VALUES (@e, @p, @r, @c)
"""

job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ScalarQueryParameter("e", "STRING", email),
        bigquery.ScalarQueryParameter("p", "STRING", hash_value),
        bigquery.ScalarQueryParameter("r", "STRING", role),
        bigquery.ScalarQueryParameter("c", "TIMESTAMP", datetime.utcnow().isoformat()),
    ]
)

client.query(query, job_config=job_config).result()

print("✅ User created successfully")
