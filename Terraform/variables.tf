variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
}

variable "ec2_ami_id" {
  description = "AMI ID for the EC2 instance"
}

variable "ec2_instance_type" {
  description = "Instance type for the EC2 instance"
}

variable "key_name" {
  description = "Name of the key pair to use for the EC2 instance"
}
