# 🔧 Git & GitHub Setup Guide

## 🎯 Quick Setup (3 Steps)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `devops-learning-project` (or your choice)
3. Description: `Complete DevOps learning environment with Docker, Kubernetes, CI/CD, and monitoring`
4. Choose: **Public** (recommended) or Private
5. **DO NOT** check "Initialize with README" (we already have one!)
6. Click **Create repository**

### Step 2: Add All Files to Git

```bash
cd "d:\study_materials\sanket\devops\New Project"

# Add all files
git add .

# Commit
git commit -m "Initial commit: Complete DevOps learning project"
```

### Step 3: Push to GitHub

```bash
# Replace YOUR-USERNAME with your GitHub username
git remote add origin https://github.com/YOUR-USERNAME/devops-learning-project.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 📋 Detailed Step-by-Step Guide

### Prerequisites

1. **Git installed** - Check with: `git --version`
2. **GitHub account** - Sign up at https://github.com
3. **Git configured** - Run these if not done:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

---

### Step 1: Configure Git (If Not Already Done)

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use GitHub email)
git config --global user.email "your.email@example.com"

# Verify
git config --global --list
```

---

### Step 2: Create GitHub Repository

#### Option A: Using GitHub Website (Easiest)

1. Go to https://github.com
2. Click **"+"** in top-right corner
3. Select **"New repository"**
4. Fill in details:
   - **Repository name**: `devops-learning-project`
   - **Description**: `Complete DevOps learning environment`
   - **Public** (recommended for learning)
   - **DO NOT** initialize with README
5. Click **"Create repository"**
6. **Copy the repository URL** (you'll need it!)

#### Option B: Using GitHub CLI (Advanced)

```bash
# Install GitHub CLI first: https://cli.github.com/

# Login to GitHub
gh auth login

# Create repository
gh repo create devops-learning-project --public --description "Complete DevOps learning environment"
```

---

### Step 3: Stage All Files

```bash
# Navigate to project
cd "d:\study_materials\sanket\devops\New Project"

# Check what will be added
git status

# Add all files
git add .

# Verify staged files
git status
```

You should see:
```
Changes to be committed:
  new file:   .github/workflows/ci-cd.yml
  new file:   .gitignore
  new file:   LOCAL_SETUP.md
  new file:   PROJECT_OVERVIEW.md
  ... (all your files)
```

---

### Step 4: Create First Commit

```bash
# Commit with a meaningful message
git commit -m "Initial commit: Complete DevOps learning project

- Python Flask REST API
- Docker & Docker Compose setup
- Kubernetes manifests
- GitHub Actions CI/CD pipeline
- Jenkins pipeline
- Terraform AWS infrastructure
- Ansible playbooks
- Prometheus & Grafana monitoring
- Complete documentation
- Python automation scripts"
```

---

### Step 5: Connect to GitHub

```bash
# Add remote (replace YOUR-USERNAME and REPO-NAME)
git remote add origin https://github.com/YOUR-USERNAME/devops-learning-project.git

# Verify remote
git remote -v
```

You should see:
```
origin  https://github.com/YOUR-USERNAME/devops-learning-project.git (fetch)
origin  https://github.com/YOUR-USERNAME/devops-learning-project.git (push)
```

---

### Step 6: Push to GitHub

```bash
# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note:** You may be prompted for GitHub credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your password!)

---

### Step 7: Verify on GitHub

1. Go to your repository: `https://github.com/YOUR-USERNAME/devops-learning-project`
2. You should see all your files!
3. The README.md will be displayed on the main page

---

## 🔐 GitHub Authentication

### Option 1: Personal Access Token (Recommended)

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name: `DevOps Learning Project`
4. Select scopes:
   - ✅ `repo` (all repo permissions)
   - ✅ `workflow` (for GitHub Actions)
5. Click **"Generate token"**
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this token as your password when pushing

### Option 2: SSH Keys (Advanced)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: https://github.com/settings/keys
# Then use SSH URL instead:
git remote set-url origin git@github.com:YOUR-USERNAME/devops-learning-project.git
```

### Option 3: GitHub CLI (Easiest)

```bash
# Install: https://cli.github.com/
gh auth login

# Then push normally - no password needed!
```

---

## 📝 Common Git Commands

### Daily Workflow

```bash
# Check status
git status

# Add specific files
git add app/app.py

# Add all changes
git add .

# Commit changes
git commit -m "feat: add new feature"

# Push to GitHub
git push

# Pull latest changes
git pull
```

### Branch Management

```bash
# Create new branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# List branches
git branch

# Merge branch
git checkout main
git merge feature/new-feature

# Delete branch
git branch -d feature/new-feature
```

### Viewing History

```bash
# View commit history
git log

# View compact history
git log --oneline

# View changes
git diff

# View file history
git log --follow app/app.py
```

---

## 🚀 Enable GitHub Actions

After pushing, GitHub Actions will automatically run!

1. Go to your repository
2. Click **"Actions"** tab
3. You'll see the CI/CD pipeline running
4. Click on the workflow to see details

The pipeline will:
- ✅ Run tests
- ✅ Build Docker image
- ✅ Run security scan
- ✅ Deploy (if configured)

---

## 📦 Update Repository

When you make changes:

```bash
# 1. Make your changes
code app/app.py

# 2. Check what changed
git status
git diff

# 3. Stage changes
git add app/app.py

# 4. Commit
git commit -m "fix: update endpoint logic"

# 5. Push
git push
```

---

## 🌿 Branching Strategy

### For Learning (Simple)

```bash
# Work directly on main
git add .
git commit -m "your changes"
git push
```

### For Production (Best Practice)

```bash
# Create feature branch
git checkout -b feature/add-monitoring

# Make changes and commit
git add .
git commit -m "feat: add monitoring dashboard"

# Push branch
git push -u origin feature/add-monitoring

# Create Pull Request on GitHub
# Merge after review
```

---

## 🔧 Useful Git Configurations

```bash
# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"

# Enable color output
git config --global color.ui auto

# Set up aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit

# Now you can use: git st, git co, git br, git cm
```

---

## 🐛 Troubleshooting

### Problem: "Permission denied"

**Solution:** Use Personal Access Token or setup SSH keys

### Problem: "Failed to push"

```bash
# Pull first, then push
git pull --rebase origin main
git push
```

### Problem: "Merge conflicts"

```bash
# View conflicts
git status

# Edit conflicting files
# Look for <<<<<<< and >>>>>>>

# After fixing
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

### Problem: "Wrong commit message"

```bash
# Change last commit message
git commit --amend -m "correct message"

# Force push (only if not shared)
git push --force
```

### Problem: "Forgot to add file"

```bash
# Add the file
git add forgotten-file.txt

# Amend last commit
git commit --amend --no-edit

# Force push (only if not shared)
git push --force
```

---

## 📊 Repository Stats

After pushing, your repo will show:

- **Languages**: Python, Dockerfile, Shell
- **Files**: 30+ files
- **Size**: ~500KB
- **Components**: 
  - Python Flask app
  - Docker configurations
  - Kubernetes manifests
  - CI/CD pipelines
  - Infrastructure as Code
  - Documentation

---

## 🎯 Next Steps

After pushing to GitHub:

1. ✅ **Add Repository Description**
   - Go to repository settings
   - Add description and topics

2. ✅ **Add Topics** (tags)
   - `devops`
   - `docker`
   - `kubernetes`
   - `python`
   - `flask`
   - `prometheus`
   - `grafana`
   - `terraform`
   - `ansible`
   - `ci-cd`

3. ✅ **Create README Badge**
   - Add build status badge
   - Add license badge

4. ✅ **Enable GitHub Pages** (optional)
   - Settings → Pages
   - Publish documentation

5. ✅ **Invite Collaborators** (optional)
   - Settings → Collaborators
   - Add team members

---

## 📜 .gitignore Explained

Your `.gitignore` file prevents these from being committed:

```
# Python
__pycache__/      # Compiled Python files
*.pyc             # Python bytecode
venv/             # Virtual environment

# Secrets
.env              # Environment variables
*.key             # Private keys
*.pem             # Certificates

# IDE
.vscode/          # VS Code settings
.idea/            # PyCharm settings

# Terraform
*.tfstate         # Terraform state files
.terraform/       # Terraform cache

# Data
data/             # Local data
logs/             # Log files
```

---

## 🎓 Git Best Practices

### Commit Messages

```bash
# Good ✅
git commit -m "feat: add user authentication"
git commit -m "fix: resolve memory leak in worker"
git commit -m "docs: update README with setup instructions"

# Bad ❌
git commit -m "changes"
git commit -m "fix stuff"
git commit -m "update"
```

### Commit Often

```bash
# Good ✅
- Small, focused commits
- Commit after each feature
- Commit working code

# Bad ❌
- Huge commits with multiple changes
- Committing broken code
- Rare commits
```

### Pull Before Push

```bash
# Always pull latest changes first
git pull origin main
git push origin main
```

---

## 🌟 Make Your Repo Stand Out

### Add Badges to README

```markdown
![Build Status](https://github.com/YOUR-USERNAME/devops-learning-project/workflows/CI/CD%20Pipeline/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
```

### Add License

Create `LICENSE` file with MIT License:
```bash
# Create LICENSE file
echo "MIT License" > LICENSE
git add LICENSE
git commit -m "docs: add MIT license"
git push
```

### Add Contributing Guidelines

Create `CONTRIBUTING.md`:
```markdown
# Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
```

---

## ✅ Checklist

Before considering your repo complete:

- [ ] All files committed
- [ ] Pushed to GitHub
- [ ] README is clear
- [ ] .gitignore configured
- [ ] GitHub Actions working
- [ ] Repository description added
- [ ] Topics/tags added
- [ ] License added (optional)
- [ ] Repository is Public
- [ ] First issue created (optional)

---

## 🎉 Success!

Once pushed, share your repository:
- **URL**: `https://github.com/YOUR-USERNAME/devops-learning-project`
- **Clone**: `git clone https://github.com/YOUR-USERNAME/devops-learning-project.git`

Add this URL to your:
- Resume/CV
- LinkedIn profile
- Portfolio website
- Job applications

**Congratulations! You now have a professional DevOps project on GitHub!** 🚀
