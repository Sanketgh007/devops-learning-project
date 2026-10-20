#!/usr/bin/env python3
"""
Local setup script - Run entire DevOps stack locally without cloud
"""

import subprocess
import sys
import time

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    banner = f"""
{Colors.BLUE}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         🏠 LOCAL DEVOPS SETUP - NO CLOUD NEEDED!        ║
║                                                          ║
║  Run the complete DevOps stack on your local machine   ║
║  • Docker Containers                                    ║
║  • Monitoring (Prometheus + Grafana)                    ║
║  • Full CI/CD Pipeline                                  ║
║  • Everything FREE and LOCAL                            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def log_step(step, message):
    print(f"\n{Colors.BOLD}[Step {step}]{Colors.END} {Colors.BLUE}{message}{Colors.END}")

def log_success(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def log_warning(message):
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")

def log_error(message):
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def run_command(command, check=True):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=check,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def check_docker():
    """Check if Docker is installed and running"""
    log_step(1, "Checking Docker...")
    
    if not run_command("docker --version", check=False):
        log_error("Docker is not installed!")
        print("\n📥 Install Docker Desktop from: https://www.docker.com/products/docker-desktop")
        return False
    
    if not run_command("docker ps", check=False):
        log_error("Docker daemon is not running!")
        print("\n🔄 Please start Docker Desktop and wait for it to be ready.")
        return False
    
    log_success("Docker is installed and running")
    return True

def check_python():
    """Check Python installation"""
    log_step(2, "Checking Python...")
    
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        log_success(f"Python {version.major}.{version.minor}.{version.micro} is installed")
        return True
    else:
        log_warning(f"Python {version.major}.{version.minor} found. Python 3.9+ recommended.")
        return True

def build_docker_image():
    """Build Docker image locally"""
    log_step(3, "Building Docker image locally...")
    
    print("   This might take a few minutes on first run...")
    result = subprocess.run(
        ["docker", "build", "-t", "devops-learning-app:latest", "-f", "docker/Dockerfile", "."],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        log_success("Docker image built successfully!")
        return True
    else:
        log_error("Failed to build Docker image")
        print(result.stderr)
        return False

def start_docker_compose():
    """Start complete stack with Docker Compose"""
    log_step(4, "Starting complete stack with Docker Compose...")
    
    print("   Starting: Flask App + Prometheus + Grafana + Node Exporter")
    result = subprocess.run(
        ["docker", "compose", "-f", "docker/docker-compose.yml", "up", "-d"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        log_success("All containers started successfully!")
        return True
    else:
        log_error("Failed to start containers")
        print(result.stderr)
        return False

def wait_for_services():
    """Wait for services to be ready"""
    log_step(5, "Waiting for services to be ready...")
    
    services = {
        "Flask App": "http://localhost:5000/health",
        "Prometheus": "http://localhost:9090",
        "Grafana": "http://localhost:3000"
    }
    
    print("   This may take 30-60 seconds...")
    time.sleep(10)
    
    for service, url in services.items():
        print(f"   • Checking {service}...", end=" ")
        for i in range(10):
            try:
                import urllib.request
                urllib.request.urlopen(url, timeout=2)
                print("✅")
                break
            except:
                time.sleep(3)
        else:
            print("⚠️  (may need more time)")
    
    log_success("Services are starting up!")
    return True

def show_access_info():
    """Show how to access services"""
    log_step(6, "Access your local DevOps stack:")
    
    print(f"""
{Colors.GREEN}
╔══════════════════════════════════════════════════════════╗
║               🎉 SUCCESS! Everything is Running!         ║
╚══════════════════════════════════════════════════════════╝
{Colors.END}
Access your services:

  📱 {Colors.BOLD}Flask Application{Colors.END}
     {Colors.BLUE}http://localhost:5000{Colors.END}
     Try: http://localhost:5000/api/tasks

  📊 {Colors.BOLD}Prometheus (Metrics){Colors.END}
     {Colors.BLUE}http://localhost:9090{Colors.END}
     Query: app_requests_total

  📈 {Colors.BOLD}Grafana (Dashboards){Colors.END}
     {Colors.BLUE}http://localhost:3000{Colors.END}
     Login: admin / admin

  💻 {Colors.BOLD}Node Exporter (System){Colors.END}
     {Colors.BLUE}http://localhost:9100{Colors.END}

{Colors.YELLOW}
📚 Next Steps:
   1. Open the URLs above in your browser
   2. Test the API: curl http://localhost:5000/api/tasks
   3. Create Grafana dashboards
   4. Read LOCAL_SETUP.md for more scenarios
{Colors.END}

{Colors.GREEN}
🛠️  Useful Commands:
   
   # View logs
   docker compose -f docker/docker-compose.yml logs -f

   # Stop all services
   docker compose -f docker/docker-compose.yml down

   # Restart services
   docker compose -f docker/docker-compose.yml restart

   # Run tests
   python scripts/health_check.py --full
{Colors.END}
    """)

def show_docker_commands():
    """Show useful Docker commands"""
    print(f"""
{Colors.BLUE}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Common Docker Commands
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.END}

# View running containers
docker compose -f docker/docker-compose.yml ps

# View logs (all services)
docker compose -f docker/docker-compose.yml logs -f

# View logs (specific service)
docker compose -f docker/docker-compose.yml logs -f app

# Stop everything
docker compose -f docker/docker-compose.yml down

# Stop and remove volumes
docker compose -f docker/docker-compose.yml down -v

# Rebuild and restart
docker compose -f docker/docker-compose.yml up -d --build

# Check resource usage
docker stats
    """)

def main():
    print_banner()
    
    print(f"\n{Colors.BOLD}This script will:{Colors.END}")
    print("  1. Check prerequisites")
    print("  2. Build Docker image locally")
    print("  3. Start complete DevOps stack")
    print("  4. No cloud, no cost, 100% local!\n")
    
    input("Press ENTER to continue...")
    
    # Check Docker
    if not check_docker():
        sys.exit(1)
    
    # Check Python
    check_python()
    
    # Build image
    if not build_docker_image():
        sys.exit(1)
    
    # Start services
    if not start_docker_compose():
        sys.exit(1)
    
    # Wait for services
    wait_for_services()
    
    # Show access info
    show_access_info()
    
    # Show Docker commands
    show_docker_commands()
    
    print(f"\n{Colors.GREEN}{'='*60}")
    print("🎉 Setup complete! Your local DevOps stack is ready!")
    print(f"{'='*60}{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Setup interrupted by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{Colors.RED}Error: {str(e)}{Colors.END}")
        sys.exit(1)
