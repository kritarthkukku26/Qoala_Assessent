variable "vpc_id" {
  description = "ID of the VPC"
}

variable "public_subnet_ids" {
  description = "List of IDs of public subnets"
  type        = list(string)
}
