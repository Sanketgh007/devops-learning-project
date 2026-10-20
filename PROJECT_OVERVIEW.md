# 📘 Complete DevOps Learning Project - Overview

## 🎯 Project Goal

Learn the entire DevOps ecosystem hands-on using a real Python Flask application with complete CI/CD, Infrastructure as Code, monitoring, and orchestration - **all for FREE!**

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     Development Layer                            │
│  • Python Flask REST API                                        │
│  • Pytest for testing                                           │
│  • Python automation scripts                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Containerization Layer                        │
│  • Docker (multi-stage builds)                                  │
│  • Docker Compose (orchestration)                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      CI/CD Pipeline Layer                        │
│  • GitHub Actions (automated testing, building, deploying)      │
│  • Jenkins (alternative pipeline)                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     Orchestration Layer                          │
│  • Kubernetes (namespaces, deployments, services)               │
│  • Health checks & probes                                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Infrastructure Layer                          │
│  • Terraform (AWS VPC, EC2, Security Groups)                    │
│  • Ansible (server configuration & deployment)                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      Monitoring Layer                            │
│  • Prometheus (metrics collection)                              │
│  • Grafana (visualization)                                      │
│  • Node Exporter (system metrics)                               │
└─────────────────────────────────────────────────────────────────┘
```

## 📂 Complete File Structure

```
New Project/
│
├── 📄 README.md                    # Main documentation
├── 📄 QUICKSTART.md                # 5-minute quick start
├── 📄 PROJECT_OVERVIEW.md          # This file
├── 📄 .gitignore                   # Git ignore rules
│
├── 📁 app/                         # Python Flask Application
│   ├── app.py                      # Main application (REST API)
│   ├── requirements.txt            # Python dependencies
│   └── tests/                      # Test suite
│       ├── __init__.py
│       └── test_app.py             # Unit tests with pytest
│
├── 📁 scripts/                     # Python Automation Scripts
│   ├── setup_environment.py        # Environment setup
│   ├── deploy.py                   # Deployment automation
│   └── health_check.py             # Health monitoring
│
├── 📁 docker/                      # Docker Configuration
│   ├── Dockerfile                  # Multi-stage Python image
│   ├── docker-compose.yml          # Full stack with monitoring
│   └── .dockerignore               # Docker ignore rules
│
├── 📁 kubernetes/                  # Kubernetes Manifests
│   ├── namespace.yaml              # Namespace definition
│   ├── deployment.yaml             # Application deployment
│   ├── service.yaml                # Service (NodePort)
│   └── configmap.yaml              # Configuration data
│
├── 📁 terraform/                   # Infrastructure as Code
│   ├── main.tf                     # AWS resources (VPC, EC2, SG)
│   ├── variables.tf                # Input variables
│   └── user-data.sh                # EC2 initialization script
│
├── 📁 ansible/                     # Configuration Management
│   ├── inventory/
│   │   └── hosts.ini               # Server inventory
│   └── playbooks/
│       ├── setup.yml               # Initial server setup
│       └── deploy.yml              # Application deployment
│
├── 📁 .github/                     # GitHub Integration
│   └── workflows/
│       └── ci-cd.yml               # GitHub Actions pipeline
│
├── 📁 jenkins/                     # Jenkins Configuration
│   └── Jenkinsfile                 # Declarative pipeline
│
├── 📁 monitoring/                  # Monitoring Stack
│   ├── prometheus/
│   │   └── prometheus.yml          # Prometheus config
│   └── grafana/
│       └── provisioning/
│           └── datasources/
│               └── prometheus.yml  # Grafana datasource
│
└── 📁 docs/                        # Documentation
    └── 01-getting-started.md       # Detailed setup guide
```

## 🔧 Components Explained

### 1. Python Flask Application (`app/`)
**What it does:**
- Simple REST API for task management
- Exposes health check endpoints
- Provides Prometheus metrics
- Easy to understand and modify

**Endpoints:**
- `GET /` - Home page
- `GET /health` - Health check
- `GET /ready` - Readiness check
- `GET /metrics` - Prometheus metrics
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task

### 2. Python Scripts (`scripts/`)

**setup_environment.py:**
- Checks prerequisites
- Creates virtual environment
- Installs dependencies
- Sets up Git hooks

**deploy.py:**
- Builds Docker images
- Runs tests
- Deploys to Docker/Kubernetes
- Pushes to registry

**health_check.py:**
- Tests application endpoints
- Verifies deployment
- Can be used in CI/CD

### 3. Docker (`docker/`)

**Dockerfile:**
- Multi-stage build (smaller images)
- Non-root user (security)
- Health checks built-in
- Production-ready with gunicorn

**docker-compose.yml:**
- Flask application
- Prometheus (metrics)
- Grafana (visualization)
- Node Exporter (system metrics)
- All networked together

### 4. Kubernetes (`kubernetes/`)

**Components:**
- **Namespace**: Isolates resources
- **Deployment**: Manages 2 replicas
- **Service**: Exposes app on NodePort 30000
- **ConfigMap**: Environment configuration

**Features:**
- Liveness & readiness probes
- Resource limits
- Rolling updates
- Self-healing

### 5. CI/CD Pipelines

**GitHub Actions (`.github/workflows/`):**
- Runs on every push
- Automated testing
- Docker image building
- Security scanning (Trivy)
- Deployment automation
- Free: 2000 minutes/month

**Jenkins (`jenkins/Jenkinsfile`):**
- Alternative to GitHub Actions
- Complete pipeline stages
- Parallel execution
- Docker integration
- Deploy to K8s or Ansible

### 6. Infrastructure as Code (`terraform/`)

**Creates:**
- AWS VPC (Virtual Private Cloud)
- Public subnet
- Internet Gateway
- Security Groups (ports: 22, 80, 5000, 9090, 3000)
- EC2 instance (t2.micro - free tier)

**Commands:**
```bash
terraform init    # Initialize
terraform plan    # Preview changes
terraform apply   # Create infrastructure
terraform destroy # Clean up
```

### 7. Configuration Management (`ansible/`)

**Playbooks:**
- `setup.yml`: Initial server configuration
- `deploy.yml`: Deploy application

**Features:**
- Installs Docker
- Clones repository
- Runs Docker Compose
- Verifies deployment

### 8. Monitoring (`monitoring/`)

**Prometheus:**
- Scrapes metrics every 15s
- Monitors Flask app
- Monitors system (Node Exporter)
- Stores time-series data

**Grafana:**
- Visualizes Prometheus data
- Pre-configured datasource
- Create custom dashboards
- Default login: admin/admin

## 🎓 Learning Objectives

### Week 1: Foundations
- [x] Understand REST APIs
- [x] Learn Python Flask basics
- [x] Write unit tests with pytest
- [x] Use virtual environments

### Week 2: Containerization
- [x] Build Docker images
- [x] Understand Dockerfile best practices
- [x] Use Docker Compose
- [x] Multi-stage builds
- [x] Container networking

### Week 3: Orchestration
- [x] Deploy to Kubernetes
- [x] Understand pods, deployments, services
- [x] Configure health checks
- [x] Manage configurations with ConfigMaps
- [x] Scale applications

### Week 4: CI/CD
- [x] Setup GitHub Actions
- [x] Write pipeline workflows
- [x] Automated testing
- [x] Image building & pushing
- [x] Continuous deployment
- [x] Jenkins pipeline (alternative)

### Week 5: Infrastructure
- [x] Learn Terraform basics
- [x] Define infrastructure as code
- [x] Manage AWS resources
- [x] State management
- [x] Plan & apply changes

### Week 6: Configuration
- [x] Learn Ansible basics
- [x] Write playbooks
- [x] Manage server configuration
- [x] Automate deployments
- [x] Inventory management

### Week 7: Monitoring
- [x] Setup Prometheus
- [x] Collect application metrics
- [x] Configure Grafana
- [x] Create dashboards
- [x] Set up alerting

## 🚀 Deployment Options

### Option 1: Local Development
```bash
python app/app.py
```
**Best for:** Initial development, debugging

### Option 2: Docker
```bash
docker build -t devops-learning-app -f docker/Dockerfile .
docker run -p 5000:5000 devops-learning-app
```
**Best for:** Testing containerization

### Option 3: Docker Compose
```bash
docker compose -f docker/docker-compose.yml up -d
```
**Best for:** Full stack with monitoring

### Option 4: Kubernetes
```bash
kubectl apply -f kubernetes/
```
**Best for:** Production-like environment

### Option 5: AWS (Terraform + Ansible)
```bash
cd terraform
terraform apply
cd ../ansible
ansible-playbook -i inventory/hosts.ini playbooks/deploy.yml
```
**Best for:** Real cloud deployment

### Option 6: CI/CD
```bash
git push origin main
```
**Best for:** Automated deployments

## 💰 Cost Breakdown (FREE!)

| Service | Free Tier | Usage |
|---------|-----------|-------|
| **GitHub** | Unlimited repos | ✅ Used for code & CI/CD |
| **GitHub Actions** | 2000 min/month | ✅ Used for pipeline |
| **Docker Hub** | 1 private repo | ✅ Used for images |
| **AWS EC2** | 750 hrs/month t2.micro | ✅ Used for hosting |
| **AWS EBS** | 30 GB/month | ✅ Used for storage |
| **Docker Desktop** | Free | ✅ Local K8s |
| **Minikube/Kind** | Free | ✅ Alternative K8s |
| **Prometheus** | Free (open source) | ✅ Monitoring |
| **Grafana** | Free (open source) | ✅ Dashboards |

**Total Monthly Cost: $0** 🎉

## 📊 Monitoring & Metrics

### Application Metrics
- `app_requests_total` - Total HTTP requests
- `app_request_latency_seconds` - Request duration

### System Metrics (Node Exporter)
- CPU usage
- Memory usage
- Disk I/O
- Network traffic

### Access Metrics
1. **Prometheus**: http://localhost:9090
   - Query: `app_requests_total`
   - Query: `rate(app_requests_total[5m])`

2. **Grafana**: http://localhost:3000
   - Create dashboard
   - Add Prometheus queries
   - Visualize data

## 🧪 Testing Strategy

### Unit Tests
```bash
pytest app/tests/ -v
```
Tests individual functions

### Integration Tests
```bash
python scripts/health_check.py --full
```
Tests complete API

### Container Tests
```bash
docker run --rm devops-learning-app pytest
```
Tests in container environment

### Deployment Tests
```bash
# K8s health check
kubectl get pods -n devops-learning
```
Verifies deployment

## 🔐 Security Features

1. **Non-root containers** - Docker runs as user 'appuser'
2. **Image scanning** - Trivy in CI/CD pipeline
3. **Secret management** - Use environment variables
4. **Security groups** - AWS firewall rules
5. **HTTPS ready** - Can add TLS/SSL

## 🎯 Success Metrics

You've mastered this when you can:

1. ✅ Explain each component's purpose
2. ✅ Deploy using all 6 methods
3. ✅ Modify app and redeploy
4. ✅ Troubleshoot issues using logs
5. ✅ Create Grafana dashboards
6. ✅ Set up AWS infrastructure
7. ✅ Configure CI/CD pipeline
8. ✅ Scale Kubernetes deployment

## 🆘 Troubleshooting

### Application won't start
```bash
# Check logs
docker logs <container-id>
kubectl logs <pod-name>

# Verify dependencies
pip install -r app/requirements.txt
```

### Port conflicts
```bash
# Find process on port
netstat -ano | findstr :5000  # Windows
lsof -ti:5000                 # Linux/Mac

# Kill process
taskkill /PID <PID> /F        # Windows
kill -9 <PID>                 # Linux/Mac
```

### Docker issues
```bash
# Restart Docker Desktop
# Clean up
docker system prune -a
```

### Kubernetes issues
```bash
# Check pod status
kubectl describe pod <pod-name> -n devops-learning

# View events
kubectl get events -n devops-learning

# Restart deployment
kubectl rollout restart deployment/app-deployment -n devops-learning
```

## 📚 Additional Resources

### Documentation
- [Docker Docs](https://docs.docker.com/)
- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Terraform Docs](https://www.terraform.io/docs/)
- [Ansible Docs](https://docs.ansible.com/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [Prometheus Docs](https://prometheus.io/docs/)

### Learning Paths
- [Docker Tutorial](https://www.docker.com/101-tutorial)
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)

## 🎉 Next Steps

1. **Start here**: `QUICKSTART.md`
2. **Detailed guide**: `docs/01-getting-started.md`
3. **Try each component**: Follow weekly plan
4. **Build something**: Add your own features
5. **Share**: Create your own repo
6. **Help others**: Document your learnings

## 💡 Pro Tips

1. **Read error messages** - They usually tell you exactly what's wrong
2. **Check logs first** - Most issues are visible in logs
3. **Start simple** - Master one tool before combining
4. **Use the scripts** - They automate repetitive tasks
5. **Monitor everything** - Grafana shows what's happening
6. **Git commit often** - Small commits are easier to debug
7. **Ask questions** - Use Stack Overflow, GitHub Issues
8. **Document as you learn** - Future you will thank you

---

## 🌟 You've Got This!

This project includes **everything** you need to learn DevOps from scratch. Take it step by step, and you'll master:

- ✅ Application development
- ✅ Containerization
- ✅ Orchestration  
- ✅ CI/CD pipelines
- ✅ Infrastructure as Code
- ✅ Configuration management
- ✅ Monitoring & observability

**Start now:**
```bash
python scripts/setup_environment.py
```

Then open `QUICKSTART.md` and choose your learning path!

Happy learning! 🚀
