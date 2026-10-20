#!/bin/bash
# User data script for EC2 instance initialization

set -e

# Update system
yum update -y

# Install Docker
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Install Git
yum install -y git

# Install Python 3
yum install -y python3 python3-pip

# Create application directory
mkdir -p /opt/app
cd /opt/app

# Clone repository (update with your repo URL)
# git clone https://github.com/yourusername/devops-learning.git .

echo "✅ Instance initialization complete!"
