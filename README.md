# Complete DevOps Learning Project 🚀

A comprehensive hands-on project to learn the entire DevOps ecosystem using a Python Flask application.

## 🎯 What You'll Learn

- **Application**: Python Flask REST API with health checks and metrics
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Kubernetes (using Minikube/Kind)
- **CI/CD**: GitHub Actions & Jenkins
- **IaC**: Terraform (AWS free tier)
- **Configuration Management**: Ansible
- **Monitoring**: Prometheus & Grafana
- **Version Control**: Git & GitHub

## 📁 Project Structure

```
.
├── app/                    # Python Flask application
│   ├── app.py             # Main application
│   ├── requirements.txt   # Python dependencies
│   └── tests/             # Unit tests
├── scripts/                # Python automation scripts
├── docker/                 # Dockerfiles and compose files
├── kubernetes/             # K8s manifests
├── terraform/              # Infrastructure as Code
├── ansible/                # Configuration management playbooks
├── .github/workflows/      # GitHub Actions CI/CD
├── jenkins/                # Jenkins pipeline
├── monitoring/             # Prometheus & Grafana configs
└── docs/                   # Step-by-step guides
```

## 🚀 Quick Start

### Prerequisites (All Free!)

1. **Git** - Version control
2. **Docker Desktop** - Container runtime (includes Kubernetes)
3. **Python 3.9+** - Application runtime
4. **VS Code** - Code editor
5. **GitHub Account** - For CI/CD and repository
6. **AWS Free Tier** (optional) - For Terraform practice

### 🏠 100% Local Setup (NO CLOUD REQUIRED!)

**Yes! You can run EVERYTHING locally without any cloud services!**

```bash
# Super Quick Start (One Command!)
python scripts/local_setup.py
```

This will:
- ✅ Build Docker image locally
- ✅ Start complete stack (App + Prometheus + Grafana)
- ✅ Everything runs on your machine
- ✅ No cloud, no cost, no credit card needed!

**Or Manual Setup:**

```bash
# 1. Navigate to project
cd "New Project"

# 2. Build Docker image locally
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# 3. Start complete stack
docker compose -f docker/docker-compose.yml up -d

# 4. Access your local stack
# App: http://localhost:5000
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3000 (admin/admin)
```

**📖 Full Guide**: See [LOCAL_SETUP.md](LOCAL_SETUP.md) for complete local workflows

### Docker Setup

```bash
# Build the Docker image
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Run with Docker
docker run -p 3000:3000 devops-learning-app:latest

# Or use Docker Compose
docker-compose -f docker/docker-compose.yml up
```

### Kubernetes Setup

```bash
# Enable Kubernetes in Docker Desktop or install Minikube

# Apply Kubernetes manifests
kubectl apply -f kubernetes/

# Check deployment
kubectl get all -n devops-learning

# Access the application
kubectl port-forward svc/app-service 3000:3000 -n devops-learning
```

## 📚 Learning Path

Follow these guides in order:

1. **[Getting Started](docs/01-getting-started.md)** - Setup your environment
2. **[Docker Basics](docs/02-docker.md)** - Containerize the application
3. **[Kubernetes Deployment](docs/03-kubernetes.md)** - Deploy to K8s
4. **[GitHub Actions](docs/04-github-actions.md)** - Automate with CI/CD
5. **[Jenkins Setup](docs/05-jenkins.md)** - Alternative CI/CD pipeline
6. **[Terraform](docs/06-terraform.md)** - Infrastructure as Code
7. **[Ansible](docs/07-ansible.md)** - Configuration Management
8. **[Monitoring](docs/08-monitoring.md)** - Prometheus & Grafana

## 🔧 Components Overview

### Application (Node.js)
- Simple Express.js REST API
- Health check endpoint (`/health`)
- Metrics endpoint (`/metrics`) for Prometheus
- Version endpoint (`/version`)

### CI/CD Pipelines
- **GitHub Actions**: Automatic build, test, and deploy on push
- **Jenkins**: Alternative pipeline with same functionality

### Infrastructure
- **Terraform**: AWS EC2, VPC, Security Groups (free tier)
- **Ansible**: Server configuration, app deployment

### Monitoring Stack
- **Prometheus**: Metrics collection
- **Grafana**: Visualization dashboards
- **Node Exporter**: System metrics

## 🎓 Key Concepts Covered

### DevOps Practices
- ✅ Continuous Integration (CI)
- ✅ Continuous Deployment (CD)
- ✅ Infrastructure as Code (IaC)
- ✅ Configuration Management
- ✅ Container Orchestration
- ✅ Monitoring & Observability
- ✅ GitOps workflow

### Technical Skills
- Writing Dockerfiles
- Creating Kubernetes manifests
- Building CI/CD pipelines
- Managing infrastructure with Terraform
- Automating with Ansible
- Setting up monitoring
- Working with metrics and logs

## 💡 Free Resources Used

- **GitHub**: Free repository and Actions (2000 minutes/month)
- **Docker Hub**: Free image registry
- **Minikube/Kind**: Local Kubernetes
- **AWS Free Tier**: 750 hours EC2 t2.micro
- **Docker Desktop**: Local development

## 🧪 Testing the Complete Flow

```bash
# 1. Make a code change
echo "// New feature" >> app/server.js

# 2. Commit and push
git add .
git commit -m "feat: add new feature"
git push

# 3. Watch GitHub Actions run automatically
# 4. See the deployment to Kubernetes
# 5. Check metrics in Grafana
```

## 🐛 Troubleshooting

See [Troubleshooting Guide](docs/09-troubleshooting.md) for common issues.

## 📖 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Ansible Documentation](https://docs.ansible.com/)
- [Prometheus Documentation](https://prometheus.io/docs/)

## 🤝 Contributing

This is a learning project. Feel free to:
- Add more features
- Improve documentation
- Share your learnings
- Create issues for questions

## 📝 License

MIT License - feel free to use for learning!

---

**Happy Learning! 🎉**

Start with `docs/01-getting-started.md` to begin your DevOps journey!
