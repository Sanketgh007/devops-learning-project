# 🏠 Complete Local Setup - No Cloud Required!

## 🎯 Yes! You Can Run Everything Locally

You can experience the **entire DevOps pipeline** without spending a penny or using any cloud services. Everything runs on your local machine using Docker!

## 📋 What You Need (All Free!)

1. **Docker Desktop** (includes Kubernetes) - https://www.docker.com/products/docker-desktop
2. **Python 3.9+** - https://www.python.org/downloads/
3. **Git** - https://git-scm.com/downloads

That's it! No AWS, no cloud accounts, no credit cards needed!

---

## 🚀 Quick Start (100% Local)

### Step 1: Setup Environment

```bash
# Navigate to project
cd "d:\study_materials\sanket\devops\New Project"

# Run setup script
python scripts/setup_environment.py

# Activate virtual environment
.\venv\Scripts\activate
```

### Step 2: Build Everything Locally

```bash
# Build Docker image locally
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Verify image was created
docker images | findstr devops-learning-app
```

### Step 3: Run Complete Stack Locally

```bash
# Start everything with Docker Compose
docker compose -f docker/docker-compose.yml up -d

# Check all containers are running
docker compose -f docker/docker-compose.yml ps
```

**Done!** 🎉 Access your local stack:
- **Application**: http://localhost:5000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)
- **Node Exporter**: http://localhost:9100

---

## 🐳 What Runs Locally in Docker

### Container Stack

```
┌─────────────────────────────────────────┐
│     Your Local Docker Environment       │
├─────────────────────────────────────────┤
│                                         │
│  📦 Flask App Container                 │
│     • Python application                │
│     • Port: 5000                        │
│     • Health checks enabled             │
│                                         │
│  📊 Prometheus Container                │
│     • Metrics collection                │
│     • Port: 9090                        │
│     • Scrapes app metrics               │
│                                         │
│  📈 Grafana Container                   │
│     • Dashboards                        │
│     • Port: 3000                        │
│     • Pre-configured datasource         │
│                                         │
│  💻 Node Exporter Container             │
│     • System metrics                    │
│     • Port: 9100                        │
│     • CPU, Memory, Disk stats           │
│                                         │
└─────────────────────────────────────────┘
        All connected via Docker network
```

---

## ☸️ Local Kubernetes Option

Docker Desktop includes Kubernetes! Use it for learning:

### Enable Kubernetes

1. Open Docker Desktop
2. Go to **Settings** → **Kubernetes**
3. Check "**Enable Kubernetes**"
4. Click "**Apply & Restart**"
5. Wait for Kubernetes indicator to turn green

### Deploy to Local Kubernetes

```bash
# Build image (Kubernetes will use it)
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Deploy to local Kubernetes
kubectl apply -f kubernetes/

# Check deployment
kubectl get all -n devops-learning

# Access the application
kubectl port-forward svc/app-service 5000:5000 -n devops-learning
```

Visit: http://localhost:5000

---

## 🔄 Local CI/CD with Jenkins (Docker)

Run Jenkins locally in Docker!

### Step 1: Run Jenkins Container

```bash
# Create Jenkins container
docker run -d \
  --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### Step 2: Get Initial Admin Password

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Step 3: Access Jenkins

Visit: http://localhost:8080

Configure your pipeline using `jenkins/Jenkinsfile`!

---

## 🎮 Complete Local Workflow

### Workflow 1: Development Mode

```bash
# 1. Write code
code app/app.py

# 2. Run locally (no Docker)
python app/app.py

# 3. Test changes
curl http://localhost:5000/api/tasks

# 4. Run tests
pytest app/tests/ -v
```

### Workflow 2: Docker Build & Test

```bash
# 1. Build image
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# 2. Run single container
docker run -d -p 5000:5000 --name my-app devops-learning-app:latest

# 3. Test
python scripts/health_check.py --full

# 4. Check logs
docker logs my-app

# 5. Stop and remove
docker stop my-app
docker rm my-app
```

### Workflow 3: Full Stack with Monitoring

```bash
# 1. Start complete stack
docker compose -f docker/docker-compose.yml up -d

# 2. View logs
docker compose -f docker/docker-compose.yml logs -f

# 3. Test application
curl http://localhost:5000/health

# 4. Check Prometheus metrics
curl http://localhost:5000/metrics

# 5. Open Grafana dashboards
# http://localhost:3000 (admin/admin)

# 6. Stop everything
docker compose -f docker/docker-compose.yml down
```

### Workflow 4: Local Kubernetes

```bash
# 1. Build image
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# 2. Deploy
kubectl apply -f kubernetes/

# 3. Watch deployment
kubectl get pods -n devops-learning -w

# 4. Check logs
kubectl logs -f deployment/app-deployment -n devops-learning

# 5. Scale up/down
kubectl scale deployment/app-deployment --replicas=3 -n devops-learning

# 6. Access app
kubectl port-forward svc/app-service 5000:5000 -n devops-learning

# 7. Delete when done
kubectl delete -f kubernetes/
```

---

## 🤖 Using Python Scripts (Easiest Way!)

### All-in-One Deploy

```bash
# Build, test, and deploy everything
python scripts/deploy.py --all
```

This will:
1. ✅ Build Docker image
2. ✅ Run all tests
3. ✅ Deploy with Docker Compose
4. ✅ Start monitoring stack

### Individual Operations

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

---

## 📊 Local Monitoring Setup

### Prometheus (Metrics Collection)

1. Start stack: `docker compose -f docker/docker-compose.yml up -d`
2. Open: http://localhost:9090
3. Try queries:
   ```
   app_requests_total
   rate(app_requests_total[5m])
   app_request_latency_seconds
   ```

### Grafana (Visualization)

1. Open: http://localhost:3000
2. Login: admin/admin
3. Data source is pre-configured!
4. Create dashboard:
   - Add panel
   - Query: `rate(app_requests_total[5m])`
   - Visualize!

---

## 🧪 Testing Locally

### Unit Tests

```bash
# Activate virtual environment
.\venv\Scripts\activate

# Run tests
pytest app/tests/ -v

# With coverage
pytest app/tests/ --cov=app --cov-report=html

# Open coverage report
start htmlcov/index.html
```

### Integration Tests

```bash
# Start application
docker compose -f docker/docker-compose.yml up -d

# Run health checks
python scripts/health_check.py --full

# Manual API testing
curl http://localhost:5000/api/tasks
curl -X POST http://localhost:5000/api/tasks -H "Content-Type: application/json" -d "{\"title\":\"Test\",\"completed\":false}"
```

### Load Testing (Optional)

```powershell
# Simple load test with PowerShell
1..100 | ForEach-Object { 
    Invoke-WebRequest http://localhost:5000/health 
}
```

Then check metrics in Prometheus!

---

## 🎓 Learning Scenarios (All Local!)

### Scenario 1: Basic Docker (15 min)
```bash
# Build
docker build -t devops-learning-app:latest -f docker/Dockerfile .

# Run
docker run -p 5000:5000 devops-learning-app:latest

# Test
curl http://localhost:5000
```

**Learn**: Dockerfiles, image layers, container lifecycle

---

### Scenario 2: Multi-Container (30 min)
```bash
# Start stack
docker compose -f docker/docker-compose.yml up -d

# Explore
docker compose -f docker/docker-compose.yml ps
docker compose -f docker/docker-compose.yml logs

# Test connectivity
docker compose -f docker/docker-compose.yml exec app curl prometheus:9090
```

**Learn**: Docker Compose, networking, volumes, service discovery

---

### Scenario 3: Kubernetes Locally (45 min)
```bash
# Deploy
kubectl apply -f kubernetes/

# Explore
kubectl get all -n devops-learning
kubectl describe pod <pod-name> -n devops-learning

# Scale
kubectl scale deployment/app-deployment --replicas=3 -n devops-learning

# Rolling update
docker build -t devops-learning-app:v2 -f docker/Dockerfile .
kubectl set image deployment/app-deployment app=devops-learning-app:v2 -n devops-learning
```

**Learn**: Deployments, services, scaling, updates, self-healing

---

### Scenario 4: CI/CD Locally (60 min)
```bash
# Start Jenkins
docker run -d -p 8080:8080 --name jenkins jenkins/jenkins:lts

# Configure pipeline with jenkins/Jenkinsfile
# Trigger builds
# Watch automation happen!
```

**Learn**: Pipeline as code, automated testing, build triggers

---

### Scenario 5: Monitoring (30 min)
```bash
# Start stack
docker compose -f docker/docker-compose.yml up -d

# Generate traffic
for ($i=0; $i -lt 100; $i++) { 
    Invoke-WebRequest http://localhost:5000/api/tasks 
}

# Watch metrics in:
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000
```

**Learn**: Metrics, monitoring, dashboards, alerting

---

## 💾 Local Data Persistence

All data is stored in Docker volumes on your machine:

```bash
# List volumes
docker volume ls

# Inspect volume
docker volume inspect devops_prometheus-data

# Backup volume (optional)
docker run --rm -v devops_prometheus-data:/data -v ${PWD}:/backup alpine tar czf /backup/prometheus-backup.tar.gz /data

# Restore volume (optional)
docker run --rm -v devops_prometheus-data:/data -v ${PWD}:/backup alpine tar xzf /backup/prometheus-backup.tar.gz -C /
```

---

## 🧹 Cleanup Commands

### Stop Everything

```bash
# Stop Docker Compose stack
docker compose -f docker/docker-compose.yml down

# Stop Kubernetes deployment
kubectl delete -f kubernetes/

# Stop individual container
docker stop <container-name>
```

### Remove Everything

```bash
# Remove containers and volumes
docker compose -f docker/docker-compose.yml down -v

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Nuclear option (remove EVERYTHING)
docker system prune -a --volumes
```

---

## 📊 Resource Usage

On a typical laptop:

| Component | CPU | RAM | Disk |
|-----------|-----|-----|------|
| Flask App | ~5% | 128MB | 200MB |
| Prometheus | ~2% | 256MB | 500MB |
| Grafana | ~3% | 128MB | 300MB |
| Node Exporter | ~1% | 32MB | 50MB |
| Kubernetes (optional) | ~10% | 2GB | 2GB |
| **Total** | **~20%** | **~2.5GB** | **~3GB** |

Runs smoothly on most modern computers!

---

## 🎯 Complete Local Learning Path

### Week 1: Docker Basics
- Build images
- Run containers
- Understand Dockerfile
- Use Docker Compose

### Week 2: Kubernetes Locally
- Deploy to local K8s
- Scale applications
- Rolling updates
- Health checks

### Week 3: CI/CD Locally
- Setup Jenkins in Docker
- Create pipelines
- Automate builds
- Run tests

### Week 4: Monitoring
- Setup Prometheus
- Configure Grafana
- Create dashboards
- Set alerts

**All running on your local machine!** No cloud needed!

---

## 🎉 Advantages of Local Setup

✅ **No Cost** - Zero cloud charges  
✅ **Fast Iteration** - Instant feedback  
✅ **No Internet Required** - Work offline  
✅ **Full Control** - Your machine, your rules  
✅ **Learn Faster** - Quick build-test cycles  
✅ **No Limits** - Experiment freely  
✅ **Privacy** - Data stays on your machine  

---

## 🚀 Get Started Now!

```bash
# 1. Setup
python scripts/setup_environment.py

# 2. Activate environment
.\venv\Scripts\activate

# 3. Deploy everything
python scripts/deploy.py --all

# 4. Access your local stack
start http://localhost:5000
start http://localhost:9090
start http://localhost:3000
```

---

## 🆘 Troubleshooting

### "Docker daemon not running"
- **Solution**: Start Docker Desktop and wait for it to fully start

### "Port already in use"
```bash
# Find and kill process
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "Out of disk space"
```bash
# Clean up Docker
docker system prune -a --volumes
```

### "Kubernetes not available"
- **Solution**: Enable Kubernetes in Docker Desktop Settings

### "Cannot pull image"
- **Solution**: You don't need to pull! Build locally:
  ```bash
  docker build -t devops-learning-app:latest -f docker/Dockerfile .
  ```

---

## 💡 Pro Tips for Local Development

1. **Use Docker Compose** - Easiest way to run full stack
2. **Watch logs** - `docker compose logs -f`
3. **Rebuild after changes** - `docker compose up -d --build`
4. **Use Python scripts** - They automate everything
5. **Start simple** - Run one container first, then full stack
6. **Monitor resources** - Docker Desktop shows CPU/RAM usage
7. **Clean up regularly** - `docker system prune`

---

## ✅ Local Setup Checklist

- [ ] Docker Desktop installed and running
- [ ] Python 3.9+ installed
- [ ] Project cloned
- [ ] Setup script completed
- [ ] Virtual environment activated
- [ ] Docker image builds successfully
- [ ] Single container runs
- [ ] Docker Compose stack runs
- [ ] Kubernetes enabled (optional)
- [ ] Can access all services
- [ ] Monitoring works
- [ ] Tests pass locally

---

## 🎓 What You Learn (Without Cloud!)

Even without cloud, you master:

- ✅ Docker containerization
- ✅ Multi-container orchestration
- ✅ Kubernetes fundamentals
- ✅ CI/CD pipelines (Jenkins)
- ✅ Monitoring & metrics
- ✅ Application deployment
- ✅ Troubleshooting
- ✅ DevOps best practices

**Cloud is optional** - 90% of DevOps skills are learned locally!

---

## 🌟 Ready to Start?

```bash
cd "d:\study_materials\sanket\devops\New Project"
python scripts/setup_environment.py
```

**Everything runs on your machine. No cloud. No credit card. No limits!** 🚀
