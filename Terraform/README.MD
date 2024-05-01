
## Directory Structure
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── modules
│ ├── vpc
│ │ ├── main.tf
│ │ ├── outputs.tf
│ │ └── variables.tf
│ ├── subnets
│ │ ├── main.tf
│ │ ├── outputs.tf
│ │ └── variables.tf
│ ├── ec2_instance
│ │ ├── main.tf
│ │ ├── outputs.tf
│ │ └── variables.tf
│ └── alb
│ ├── main.tf
│ └── variables.tf


- **main.tf**: The main Terraform configuration file that defines the infrastructure resources.
- **variables.tf**: Defines input variables used in the Terraform configuration.
- **outputs.tf**: Defines outputs to display after Terraform applies the configuration.
- **terraform.tfvars**: Contains the values for input variables.
- **modules**: Directory containing submodules for VPC, subnets, EC2 instance, and ALB.
  - **vpc**: Module for creating the VPC.
  - **subnets**: Module for creating public and private subnets.
  - **ec2_instance**: Module for creating an EC2 instance.
  - **alb**: Module for creating an Application Load Balancer.

## Usage

1. Install Terraform: [Download Terraform](https://www.terraform.io/downloads.html) and follow the installation instructions.

2. Set up AWS credentials: Configure your AWS credentials using environment variables, AWS CLI, or any other method supported by Terraform.

3. Initialize Terraform: Run `terraform init` in the project directory to initialize Terraform and download the necessary providers.

4. Adjust configuration: Update `terraform.tfvars` with your desired values for input variables.

5. Apply configuration: Run `terraform apply` to apply the Terraform configuration and create the infrastructure.

6. Clean up: After testing, you can destroy the created infrastructure by running `terraform destroy`.

