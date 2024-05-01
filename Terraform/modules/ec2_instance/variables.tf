variable "ami_id" {
  description = "AMI ID for the EC2 instance"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
}

variable "subnet_id" {
  description = "ID of the subnet where the EC2 instance will be launched"
}

variable "key_name" {
  description = "Name of the key pair to use for the EC2 instance"
}
