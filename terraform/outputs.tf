// terraform/outputs.tf
output "service_account_email" {
  value = google_service_account.mcp_sa.email
}
output "vm_ip" {
  value = google_compute_instance.vm.network_interface[0].access_config[0].nat_ip
}
