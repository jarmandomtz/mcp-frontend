# terraform steps

Initialize terraform and execute the resources creation

```shell
# Authentication
gcloud auth login
gcloud config set project thematic-bee-473421-i7
gcloud auth application-default login
gcloud services enable compute.googleapis.com bigquery.googleapis.com iam.googleapis.com

# Terraform
terraform -v
terraform init
terraform validate
terraform plan -var="project_id=thematic-bee-473421-i7"
terraform apply -var="project_id=thematic-bee-473421-i7"
...
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:
service_account_email = "mcp-sre-assistant-sa@thematic-bee-473421-i7.iam.gserviceaccount.com"
vm_ip = "34.63.147.244"

```

## Errors

<details close>
<summary>Recreate just the VM due errors on startuo.sh script</summary>

```shell
# Get state resources
terraform state list
google_bigquery_dataset.dataset
google_bigquery_table.users
google_compute_firewall.allow_http
google_compute_instance.vm
google_project_iam_binding.bq_access
google_service_account.mcp_sa

# Regenerate VM
terraform apply -var="project_id=thematic-bee-473421-i7" -replace="google_compute_instance.vm" -auto-approve
...
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:
service_account_email = "mcp-sre-assistant-sa@thematic-bee-473421-i7.iam.gserviceaccount.com"
vm_ip = "34.63.147.244"
```

</details>

<details close>
<summary>Troubleshoot errors on the instance logs</summary>

```shell

# Get instance logs
gcloud auth login
gcloud compute --project=thematic-bee-473421-i7 instances get-serial-port-output mcp-sre-assistant-vm --zone=us-central1-a --port=1

# Connect to the instance
gcloud compute ssh --zone "us-central1-a" "mcp-sre-assistant-vm" --project "thematic-bee-473421-i7"
```

On the instance shell

```shell
# System service status
systemctl status mcp.service

tree /opt/mcp-sre-assistant
```

</details>