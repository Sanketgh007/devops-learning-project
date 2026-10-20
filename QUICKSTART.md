# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## 🎯 Goal

By the end of this guide, you'll have:
- ✅ A running Flask application
- ✅ Complete monitoring stack (Prometheus + Grafana)
- ✅ Experience with Docker, Kubernetes, CI/CD, and more

## 🚀 Super Quick Start (3 Commands!)

```bash
# 1. Setup environment
python scripts/setup_environment.py

# 2. Activate virtual environment (Windows)
.\venv\Scripts\activate

# 3. Deploy everything with Docker Compose
python scripts/deploy.py --all
```

That's it! 🎉

Access your stack:
- **App**: http://localhost:5000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (user: admin, pass: admin)

## 📚 Learning Paths

### Path 1: Local Development (Fastest)
**Time: 5 minutes**

```bash
# Run locally with Python
cd app
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

**What you'll learn:**
- Python Flask basics
- REST API development
- Application structure

---

### Path 2: Docker (Most Popular)
**Time: 10 minutes**

```bash
# Deploy with full monitoring stack
docker compose -f docker/docker-compose.yml up -d

# Check logs
docker compose -f docker/docker-compose.yml logs -f app

# Stop when done
docker compose -f docker/docker-compose.yml down
```

**What you'll learn:**
- Docker containerization
- Docker Compose orchestration
- Multi-container applications
- Prometheus metrics
- Grafana dashboards

---

### Path 3: Kubernetes (Most Powerful)
**Time: 15 minutes**

```bash
# Enable Kubernetes in Docker Desktop first!

# Build image
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Deploy to Kubernetes
kubectl apply -f kubernetes/

# Check status
kubectl get all -n devops-learning

# Access app
kubectl port-forward svc/app-service 5000:5000 -n devops-learning
```

**What you'll learn:**
- Kubernetes deployments
- Services & networking
- ConfigMaps
- Health checks & probes
- Container orchestration

---

### Path 4: CI/CD with GitHub Actions
**Time: 20 minutes**

```bash
# 1. Create GitHub repository
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

# 2. GitHub Actions will run automatically!
# Go to GitHub → Actions tab to watch
```

**What you'll learn:**
- Continuous Integration
- Automated testing
- Docker image building
- Security scanning
- Deployment automation

---

### Path 5: Infrastructure as Code (Terraform)
**Time: 30 minutes**

```bash
# Prerequisites: AWS account with free tier

cd terraform

# Initialize Terraform
terraform init

# Plan infrastructure
terraform plan

# Create infrastructure
terraform apply

# Destroy when done (to avoid charges)
terraform destroy
```

**What you'll learn:**
- Infrastructure as Code
- AWS VPC, EC2, Security Groups
- Terraform basics
- Cloud resource management

---

### Path 6: Configuration Management (Ansible)
**Time: 25 minutes**

```bash
# Prerequisites: A server (EC2 instance from Terraform!)

cd ansible

# Edit inventory with your server IP
nano inventory/hosts.ini

# Test connection
ansible app_servers -i inventory/hosts.ini -m ping

# Initial setup
ansible-playbook -i inventory/hosts.ini playbooks/setup.yml

# Deploy application
ansible-playbook -i inventory/hosts.ini playbooks/deploy.yml
```

**What you'll learn:**
- Configuration management
- Ansible playbooks
- Server automation
- Deployment automation

---

### Path 7: Monitoring (Prometheus + Grafana)
**Time: 15 minutes**

```bash
# Deploy with Docker Compose (includes monitoring)
docker compose -f docker/docker-compose.yml up -d

# Access Grafana: http://localhost:3000
# Username: admin
# Password: admin

# 1. Add Prometheus as data source (already configured!)
# 2. Create dashboard
# 3. Add panels for:
#    - Request count
#    - Request latency
#    - System metrics
```

**What you'll learn:**
- Metrics collection
- Prometheus queries (PromQL)
- Grafana dashboards
- Application monitoring
- Alerting setup

---

## 🎓 Complete DevOps Journey

Follow this order for best learning experience:

```
Week 1: Basics
├── Day 1-2: Local Development + Docker
├── Day 3-4: Docker Compose + Monitoring
└── Day 5-7: Kubernetes

Week 2: Automation
├── Day 8-10: GitHub Actions CI/CD
├── Day 11-12: Jenkins Pipeline
└── Day 13-14: Testing & Quality

Week 3: Infrastructure
├── Day 15-17: Terraform (AWS)
├── Day 18-19: Ansible
└── Day 20-21: Cloud Deployment

Week 4: Advanced
├── Day 22-24: Production Setup
├── Day 25-26: Monitoring & Logging
└── Day 27-30: Best Practices & Review
```

## 🧪 Test Everything Works

```bash
# Run automated tests
pytest app/tests/ -v

# Run health checks
python scripts/health_check.py --full

# Check Docker deployment
docker compose -f docker/docker-compose.yml ps

# Check Kubernetes deployment
kubectl get all -n devops-learning
```

## 📊 API Examples

```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Create a new task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Deploy to production","completed":false}'

# Get application info
curl http://localhost:5000/api/info

# Check health
curl http://localhost:5000/health

# View metrics (Prometheus format)
curl http://localhost:5000/metrics
```

## 🛠️ Useful Commands

### Docker
```bash
# View logs
docker compose -f docker/docker-compose.yml logs -f app

# Restart service
docker compose -f docker/docker-compose.yml restart app

# Clean up
docker compose -f docker/docker-compose.yml down -v
docker system prune -a
```

### Kubernetes
```bash
# View pods
kubectl get pods -n devops-learning

# View logs
kubectl logs -f deployment/app-deployment -n devops-learning

# Describe deployment
kubectl describe deployment app-deployment -n devops-learning

# Delete everything
kubectl delete -f kubernetes/
```

### Python Scripts
```bash
# Build only
python scripts/deploy.py --build

# Test only
python scripts/deploy.py --test

# Deploy to Docker
python scripts/deploy.py --deploy docker

# Deploy to Kubernetes
python scripts/deploy.py --deploy k8s

# Clean up everything
python scripts/deploy.py --cleanup
```

## 🎯 Learning Checklist

- [ ] Run application locally
- [ ] Build Docker image
- [ ] Run with Docker Compose
- [ ] Deploy to Kubernetes
- [ ] Setup GitHub Actions
- [ ] Configure Jenkins pipeline
- [ ] Create AWS infrastructure with Terraform
- [ ] Deploy with Ansible
- [ ] Setup Prometheus monitoring
- [ ] Create Grafana dashboards
- [ ] Run automated tests
- [ ] Understand CI/CD flow

## 🆘 Common Issues

### "Port already in use"
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### "Docker daemon not running"
- Start Docker Desktop
- Wait for it to fully start
- Try your command again

### "Module not found"
```bash
# Make sure virtual environment is activated
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac

# Reinstall dependencies
pip install -r app/requirements.txt
```

### "Kubernetes not available"
- Enable Kubernetes in Docker Desktop settings
- Wait for it to start (green indicator)
- Verify: `kubectl version --client`

## 📖 What's Next?

1. **Read Full Docs**: Start with `docs/01-getting-started.md`
2. **Experiment**: Change code, rebuild, redeploy
3. **Monitor**: Watch metrics in Grafana
4. **Learn**: Follow the weekly learning plan above
5. **Build**: Create your own features
6. **Share**: Push to GitHub and show off!

## 💡 Pro Tips

1. **Start Simple**: Master each tool individually before combining
2. **Read Logs**: They tell you exactly what's wrong
3. **Use Scripts**: The Python scripts automate repetitive tasks
4. **Check Health**: Use `/health` endpoint to verify deployments
5. **Monitor Everything**: Grafana dashboards show you what's happening
6. **Iterate Fast**: Make small changes and test immediately
7. **Learn by Doing**: Break things, fix them, learn from mistakes

## 🎉 Success Criteria

You'll know you're successful when you can:

- ✅ Explain what each component does
- ✅ Deploy the application 3 different ways
- ✅ Troubleshoot issues using logs and metrics
- ✅ Make code changes and deploy them
- ✅ Set up monitoring and understand the metrics
- ✅ Automate deployment with CI/CD
- ✅ Manage infrastructure with code

---

**Ready to start?** Run this now:

```bash
python scripts/setup_environment.py
```

Then pick your learning path above! 🚀
