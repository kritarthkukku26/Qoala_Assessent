resource "aws_subnet" "subnets" {
  count             = length(var.subnet_cidrs)
  vpc_id            = var.subnet_vpc_id
  cidr_block        = var.subnet_cidrs[count.index]
  availability_zone = "us-east-1a" # Modify according to your desired availability zone

  tags = {
    Name = "${var.subnet_type}-subnet-${count.index + 1}"
  }
}
