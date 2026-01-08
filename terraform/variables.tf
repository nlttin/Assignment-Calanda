variable "subscription_id" {
  type        = string
  description = "The Azure Subscription ID"
}
variable "resource_group_name" {
  description = "Caladan Resource Group Name"
  type        = string
  default     = "latency-monitor-rg"
}

variable "location" {
  description = "Caladan Azure region"
  type        = string
  default     = "East US"
}

variable "vm_size" {
  description = "Size of the Virtual Machines"
  type        = string
  default     = "Standard_B1s"
}

variable "admin_username" {
  description = "Admin username for the VMs"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key_path" {
  description = "Path to the SSH public key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}