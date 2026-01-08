# Assignment-Calanda
Calanda
# Azure Latency Test Infrastructure

This project uses **Terraform** to deploy a network latency testing environment on Microsoft Azure. It sets up two Ubuntu 24.04 LTS virtual machines within a private Virtual Network (VNet) to measure internal network performance.

##  Architecture
The infrastructure includes:
- **Resource Group**: `devops-latency-test`
- **Virtual Network**: `10.0.0.0/16`
- **Subnet**: `10.0.1.0/24`
- **Virtual Machines**: 
  - `monitoring-server` (10.0.1.4)
  - `target-server` (10.0.1.5)
- **Networking**: Public IPs for both VMs and a Network Security Group (NSG) allowing SSH (22) and App Port (8000).



##  Prerequisites
- [Terraform](https://www.terraform.io/downloads.html) (v1.0+)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- SSH Key Pair (`~/.ssh/id_rsa.pub`)

##  Deployment Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nlttin/Assignment-Calanda.git](https://github.com/nlttin/Assignment-Calanda.git)
   cd Assignment-Calanda/terraform

Steps: 
bash:
az login
Initialize and Apply:
terraform init
terraform plan
terraform apply -auto-approve
**Testing Latency
**Once the deployment is complete, follow these steps to test the latency:

**SSH into the Monitoring Server:

Bash

ssh azureuser@<MONITORING_SERVER_PUBLIC_IP>
**Ping the Target Server (Internal):

Bash

ping 10.0.1.5