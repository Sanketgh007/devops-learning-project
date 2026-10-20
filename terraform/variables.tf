variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "ami_id" {
  description = "AMI ID for EC2 instance (Amazon Linux 2)"
  type        = string
  # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
  # Update this with the latest AMI ID for your region
  default = "ami-0c55b159cbfafe1f0"
}

variable "key_name" {
  description = "EC2 key pair name"
  type        = string
  default     = "devops-learning-key"
}
