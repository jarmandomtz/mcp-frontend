// terraform/main.tf
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_service_account" "mcp_sa" {
  account_id   = "mcp-sre-assistant-sa"
  display_name = "MCP SRE Assistant Service Account"
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "mcp_sre_assistant"
  location                    = var.bq_location
  delete_contents_on_destroy  = false
}

resource "google_bigquery_table" "users" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = "users"
  schema     = <<EOF
[
  {"name":"email","type":"STRING","mode":"REQUIRED"},
  {"name":"password_hash","type":"STRING","mode":"REQUIRED"},
  {"name":"role","type":"STRING","mode":"REQUIRED"},
  {"name":"created_at","type":"TIMESTAMP","mode":"REQUIRED"}
]
EOF
}

resource "google_compute_instance" "vm" {
  name         = "mcp-sre-assistant-vm"
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "projects/debian-cloud/global/images/family/debian-12"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  service_account {
    email  = google_service_account.mcp_sa.email
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }

  metadata_startup_script = file("${path.module}/startup.sh")
}

resource "google_project_iam_binding" "bq_access" {
  project = var.project_id
  role    = "roles/bigquery.user"
  members = [
    "serviceAccount:${google_service_account.mcp_sa.email}"
  ]
}

resource "google_project_iam_binding" "logging_logwriter" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  members = [
    "serviceAccount:${google_service_account.mcp_sa.email}"
  ]
}

resource "google_compute_firewall" "allow_http" {
  name    = "mcp-sre-assistant-allow-http"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "8000", "8002"]
  }

  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
}
