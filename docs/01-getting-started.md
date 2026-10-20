# Getting Started with DevOps Learning Project

Welcome! This guide will help you set up your complete DevOps learning environment.

## 📋 Prerequisites

Before starting, ensure you have these tools installed:

### Required Tools

1. **Python 3.9+**
   - Download: https://www.python.org/downloads/
   - Verify: `python --version`

2. **Git**
   - Download: https://git-scm.com/downloads
   - Verify: `git --version`

3. **Docker Desktop**
   - Download: https://www.docker.com/products/docker-desktop
   - Includes Kubernetes
   - Verify: `docker --version` and `docker compose version`

4. **VS Code** (recommended)
   - Download: https://code.visualstudio.com/

### Optional Tools

5. **kubectl** (for Kubernetes)
   - Download: https://kubernetes.io/docs/tasks/tools/
   - Verify: `kubectl version --client`

6. **Terraform** (for IaC)
   - Download: https://www.terraform.io/downloads
   - Verify: `terraform --version`

7. **AWS CLI** (for cloud deployments)
   - Download: https://aws.amazon.com/cli/
   - Verify: `aws --version`

## 🚀 Quick Setup

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd "New Project"
```

### Step 2: Run Setup Script

```bash
# This will check prerequisites and set up your environment
python scripts/setup_environment.py
```

The script will:
- ✅ Check all prerequisites
- ✅ Create Python virtual environment
- ✅ Install dependencies
- ✅ Create necessary directories
- ✅ Setup Git hooks

### Step 3: Activate Virtual Environment

**Windows:**
```powershell
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

## 🧪 Test the Application Locally

### Run without Docker

```bash
cd app
python app.py
```

Visit: http://localhost:5000

### Test Endpoints

```bash
# Health check
curl http://localhost:5000/health

# Get tasks
curl http://localhost:5000/api/tasks

# Create a task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn DevOps","completed":false}'
```

## 🐳 Run with Docker

### Build and Run

```bash
# Build the image
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Run the container
docker run -p 5000:5000 devops-learning-app:latest
```

### Or use Docker Compose (with monitoring stack)

```bash
docker compose -f docker/docker-compose.yml up -d
```

Access:
- **Application**: http://localhost:5000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

## ☸️ Run with Kubernetes

### Enable Kubernetes in Docker Desktop

1. Open Docker Desktop
2. Go to Settings → Kubernetes
3. Check "Enable Kubernetes"
4. Click "Apply & Restart"

### Deploy to Kubernetes

```bash
# Build the image first
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Apply Kubernetes manifests
kubectl apply -f kubernetes/

# Check deployment
kubectl get all -n devops-learning

# Access the application
kubectl port-forward svc/app-service 5000:5000 -n devops-learning
```

## 🧪 Run Tests

```bash
# Run all tests
pytest app/tests/ -v

# Run with coverage
pytest app/tests/ --cov=app --cov-report=html

# View coverage report
# Open htmlcov/index.html in your browser
```

## 🤖 Use Automation Scripts

### Deploy Script

```bash
# Build, test, and deploy with one command
python scripts/deploy.py --all

# Or run individual steps:
python scripts/deploy.py --build
python scripts/deploy.py --test
python scripts/deploy.py --deploy docker
```

### Health Check Script

```bash
# Quick health check
python scripts/health_check.py

# Full check (all endpoints)
python scripts/health_check.py --full

# Check custom URL
python scripts/health_check.py --url http://example.com:5000
```

## 📂 Project Structure

```
New Project/
├── app/                    # Python Flask application
│   ├── app.py             # Main application
│   ├── requirements.txt   # Dependencies
│   └── tests/             # Unit tests
├── scripts/                # Python automation scripts
│   ├── setup_environment.py
│   ├── deploy.py
│   └── health_check.py
├── docker/                 # Docker configuration
│   ├── Dockerfile
│   └── docker-compose.yml
├── kubernetes/             # K8s manifests
├── terraform/              # Infrastructure as Code
├── ansible/                # Configuration management
├── .github/workflows/      # GitHub Actions
├── jenkins/                # Jenkins pipeline
└── monitoring/             # Prometheus & Grafana
```

## 🎯 Next Steps

Now that your environment is set up, follow these guides:

1. **[Docker Deep Dive](02-docker.md)** - Learn containerization
2. **[Kubernetes Deployment](03-kubernetes.md)** - Orchestrate containers
3. **[GitHub Actions CI/CD](04-github-actions.md)** - Automate workflows
4. **[Jenkins Pipeline](05-jenkins.md)** - Alternative CI/CD
5. **[Terraform AWS](06-terraform.md)** - Infrastructure as Code
6. **[Ansible Configuration](07-ansible.md)** - Configuration management
7. **[Monitoring Setup](08-monitoring.md)** - Prometheus & Grafana

## 🐛 Troubleshooting

### Python Virtual Environment Issues

```bash
# Windows: If scripts fail to run
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Recreate virtual environment
rm -rf venv
python -m venv venv
```

### Docker Issues

```bash
# Check Docker is running
docker ps

# Clean up Docker resources
docker system prune -a
```

### Port Already in Use

```bash
# Windows: Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:5000 | xargs kill -9
```

## 💡 Tips

1. **Always activate virtual environment** before running Python scripts
2. **Read error messages carefully** - they usually tell you what's wrong
3. **Check logs** if something isn't working
4. **Start simple** - test locally before deploying to Docker/K8s
5. **One step at a time** - don't try to learn everything at once

## 🆘 Getting Help

- Check the [Troubleshooting Guide](09-troubleshooting.md)
- Review project documentation
- Search for error messages online
- Check tool-specific documentation

## ✅ Checklist

- [ ] All prerequisites installed
- [ ] Setup script completed successfully
- [ ] Virtual environment activated
- [ ] Application runs locally
- [ ] Tests pass
- [ ] Docker image builds successfully
- [ ] Docker Compose works
- [ ] Ready to learn!

---

**Next**: Continue to [Docker Deep Dive](02-docker.md) →
