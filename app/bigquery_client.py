# app/bigquery_client.py
from google.cloud import bigquery
from app.settings import settings

def get_bq_client():
    if settings.gcp_sa_credentials_json:
        return bigquery.Client.from_service_account_json(settings.gcp_sa_credentials_json)
    return bigquery.Client(project=settings.project_id)

def fetch_user(email: str):
    client = get_bq_client()
    query = f"""
    SELECT email, password_hash, role
    FROM `{settings.project_id}.{settings.bq_dataset}.{settings.bq_users_table}`
    WHERE email = @email
    LIMIT 1
    """
    job = client.query(
        query,
        job_config=bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("email", "STRING", email)]
        ),
    )
    rows = list(job.result())
    return rows[0] if rows else None
