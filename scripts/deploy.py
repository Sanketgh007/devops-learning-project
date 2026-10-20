#!/usr/bin/env python3
"""
Deployment automation script
Handles building, testing, and deploying the application
"""

import subprocess
import sys
import argparse
import os
from datetime import datetime

class Colors:
    """ANSI color codes"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'

def log_info(message):
    """Log info message"""
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.END}")

def log_success(message):
    """Log success message"""
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def log_warning(message):
    """Log warning message"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")

def log_error(message):
    """Log error message"""
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def run_command(command, cwd=None, check=True):
    """Run a shell command and return the result"""
    log_info(f"Running: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=check,
            capture_output=True,
            text=True
        )
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        log_error(f"Command failed with exit code {e.returncode}")
        if e.stderr:
            print(e.stderr)
        if check:
            sys.exit(1)
        return e

def build_docker_image(tag="latest"):
    """Build Docker image"""
    log_info("Building Docker image...")
    image_name = f"devops-learning-app:{tag}"
    
    result = run_command([
        "docker", "build",
        "-t", image_name,
        "-f", "docker/Dockerfile",
        "."
    ])
    
    if result.returncode == 0:
        log_success(f"Docker image built: {image_name}")
        return image_name
    return None

def run_tests():
    """Run application tests"""
    log_info("Running tests...")
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        log_warning("Virtual environment not found. Creating one...")
        run_command([sys.executable, "-m", "venv", "venv"])
    
    # Install dependencies
    log_info("Installing dependencies...")
    pip_path = "venv\\Scripts\\pip.exe" if os.name == 'nt' else "venv/bin/pip"
    run_command([pip_path, "install", "-r", "app/requirements.txt"])
    
    # Run pytest
    python_path = "venv\\Scripts\\python.exe" if os.name == 'nt' else "venv/bin/python"
    result = run_command([
        python_path, "-m", "pytest",
        "app/tests/",
        "-v",
        "--cov=app",
        "--cov-report=term-missing"
    ], check=False)
    
    if result.returncode == 0:
        log_success("All tests passed!")
        return True
    else:
        log_error("Tests failed!")
        return False

def deploy_to_docker_compose():
    """Deploy using Docker Compose"""
    log_info("Deploying with Docker Compose...")
    
    # Stop existing containers
    run_command([
        "docker-compose",
        "-f", "docker/docker-compose.yml",
        "down"
    ], check=False)
    
    # Start new containers
    result = run_command([
        "docker-compose",
        "-f", "docker/docker-compose.yml",
        "up", "-d", "--build"
    ])
    
    if result.returncode == 0:
        log_success("Deployed with Docker Compose!")
        log_info("Application: http://localhost:5000")
        log_info("Prometheus: http://localhost:9090")
        log_info("Grafana: http://localhost:3000 (admin/admin)")
        return True
    return False

def deploy_to_kubernetes():
    """Deploy to Kubernetes"""
    log_info("Deploying to Kubernetes...")
    
    # Apply Kubernetes manifests
    result = run_command([
        "kubectl", "apply",
        "-f", "kubernetes/"
    ])
    
    if result.returncode == 0:
        log_success("Deployed to Kubernetes!")
        log_info("Checking deployment status...")
        run_command([
            "kubectl", "get", "all",
            "-n", "devops-learning"
        ])
        return True
    return False

def push_to_registry(image_name, registry="docker.io"):
    """Push image to container registry"""
    log_info(f"Pushing {image_name} to {registry}...")
    
    # Tag for registry
    registry_image = f"{registry}/{image_name}"
    run_command(["docker", "tag", image_name, registry_image])
    
    # Push to registry
    result = run_command(["docker", "push", registry_image])
    
    if result.returncode == 0:
        log_success(f"Image pushed to {registry}")
        return True
    return False

def cleanup():
    """Clean up resources"""
    log_info("Cleaning up...")
    
    # Remove Docker containers
    run_command([
        "docker-compose",
        "-f", "docker/docker-compose.yml",
        "down", "-v"
    ], check=False)
    
    # Clean up Kubernetes resources
    run_command([
        "kubectl", "delete",
        "-f", "kubernetes/"
    ], check=False)
    
    log_success("Cleanup complete!")

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(description="DevOps Learning App Deployment Script")
    parser.add_argument('--build', action='store_true', help='Build Docker image')
    parser.add_argument('--test', action='store_true', help='Run tests')
    parser.add_argument('--deploy', choices=['docker', 'k8s'], help='Deploy target')
    parser.add_argument('--push', action='store_true', help='Push to registry')
    parser.add_argument('--tag', default='latest', help='Docker image tag')
    parser.add_argument('--registry', default='docker.io', help='Container registry')
    parser.add_argument('--cleanup', action='store_true', help='Clean up resources')
    parser.add_argument('--all', action='store_true', help='Build, test, and deploy')
    
    args = parser.parse_args()
    
    # Print banner
    print(f"\n{Colors.BLUE}{'='*60}")
    print("🚀 DevOps Learning App - Deployment Script")
    print(f"{'='*60}{Colors.END}\n")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        if args.cleanup:
            cleanup()
            return
        
        image_name = None
        
        # Build
        if args.build or args.all:
            image_name = build_docker_image(args.tag)
            if not image_name:
                log_error("Build failed!")
                sys.exit(1)
        
        # Test
        if args.test or args.all:
            if not run_tests():
                log_error("Tests failed!")
                sys.exit(1)
        
        # Deploy
        if args.deploy or args.all:
            deploy_target = args.deploy or 'docker'
            if deploy_target == 'docker':
                if not deploy_to_docker_compose():
                    log_error("Docker deployment failed!")
                    sys.exit(1)
            elif deploy_target == 'k8s':
                if not deploy_to_kubernetes():
                    log_error("Kubernetes deployment failed!")
                    sys.exit(1)
        
        # Push
        if args.push and image_name:
            if not push_to_registry(image_name, args.registry):
                log_error("Push failed!")
                sys.exit(1)
        
        print(f"\n{Colors.GREEN}{'='*60}")
        print("🎉 Deployment completed successfully!")
        print(f"{'='*60}{Colors.END}\n")
        
    except KeyboardInterrupt:
        log_warning("\nDeployment interrupted by user")
        sys.exit(1)
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
