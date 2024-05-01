variable "subnet_vpc_id" {
  description = "ID of the VPC"
}

variable "subnet_cidrs" {
  description = "CIDR blocks for subnets"
  type        = list(string)
}

variable "subnet_type" {
  description = "Type of subnets (public/private)"
}


