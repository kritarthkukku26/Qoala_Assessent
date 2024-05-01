provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source        = "./modules/vpc"
  vpc_cidr      = var.vpc_cidr
}

module "public_subnets" {
  source           = "./modules/subnets"
  subnet_vpc_id    = module.vpc.vpc_id
  subnet_cidrs     = var.public_subnet_cidrs
  subnet_type      = "public"
}


module "private_subnets" {
  source            = "./modules/subnets"
  subnet_vpc_id     = module.vpc.vpc_id
  subnet_cidrs      = var.private_subnet_cidrs
  subnet_type       = "private"
}

module "ec2_instance" {
  source       = "./modules/ec2_instance"
  subnet_id    = module.private_subnets.subnet_ids[0] 
  key_name     = var.key_name
  ami_id       = var.ec2_ami_id
  instance_type = var.ec2_instance_type
}


module "alb" {
  source                  = "./modules/alb"
  vpc_id                  = module.vpc.vpc_id
  public_subnet_ids       = module.public_subnets.subnet_ids
}