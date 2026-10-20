#!/usr/bin/env python3
"""
Environment setup script
Checks prerequisites and sets up the development environment
"""

import subprocess
import sys
import os
import platform

def check_command(command):
    """Check if a command is available"""
    try:
        subprocess.run(
            [command, "--version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def print_header(text):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def check_prerequisites():
    """Check all prerequisites"""
    print_header("Checking Prerequisites")
    
    prerequisites = {
        'Python': ('python', 'https://www.python.org/downloads/'),
        'Git': ('git', 'https://git-scm.com/downloads'),
        'Docker': ('docker', 'https://www.docker.com/products/docker-desktop'),
        'kubectl': ('kubectl', 'https://kubernetes.io/docs/tasks/tools/'),
    }
    
    results = {}
    
    for name, (command, url) in prerequisites.items():
        if check_command(command):
            print(f"✅ {name} is installed")
            results[name] = True
        else:
            print(f"❌ {name} is NOT installed")
            print(f"   Install from: {url}")
            results[name] = False
    
    return results

def create_virtual_environment():
    """Create Python virtual environment"""
    print_header("Setting up Python Virtual Environment")
    
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Dependencies")
    
    pip_path = "venv\\Scripts\\pip.exe" if os.name == 'nt' else "venv/bin/pip"
    
    if not os.path.exists(pip_path):
        print("❌ Virtual environment not found. Run setup first.")
        return False
    
    try:
        print("Installing application dependencies...")
        subprocess.run(
            [pip_path, "install", "-r", "app/requirements.txt"],
            check=True
        )
        print("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def create_directories():
    """Create necessary directories"""
    print_header("Creating Directory Structure")
    
    directories = [
        'logs',
        'data',
        'monitoring/prometheus',
        'monitoring/grafana/provisioning/dashboards',
        'monitoring/grafana/provisioning/datasources',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")
    
    return True

def setup_git_hooks():
    """Setup Git hooks"""
    print_header("Setting up Git Hooks")
    
    if not os.path.exists('.git'):
        print("⚠️  Not a git repository. Run 'git init' first.")
        return False
    
    # Pre-commit hook
    pre_commit_hook = """#!/bin/sh
# Pre-commit hook: Run tests before commit

echo "Running tests before commit..."
python scripts/deploy.py --test

if [ $? -ne 0 ]; then
    echo "❌ Tests failed. Commit aborted."
    exit 1
fi

echo "✅ Tests passed. Proceeding with commit."
exit 0
"""
    
    hook_path = ".git/hooks/pre-commit"
    try:
        with open(hook_path, 'w') as f:
            f.write(pre_commit_hook)
        
        # Make executable (Unix-like systems)
        if os.name != 'nt':
            os.chmod(hook_path, 0o755)
        
        print("✅ Git hooks configured")
        return True
    except Exception as e:
        print(f"❌ Failed to setup git hooks: {e}")
        return False

def display_next_steps():
    """Display next steps"""
    print_header("Setup Complete! 🎉")
    
    activate_cmd = "venv\\Scripts\\activate" if os.name == 'nt' else "source venv/bin/activate"
    
    print("Next steps:\n")
    print(f"1. Activate virtual environment:")
    print(f"   {activate_cmd}\n")
    print("2. Run the application:")
    print("   python app/app.py\n")
    print("3. Or deploy with Docker:")
    print("   python scripts/deploy.py --all\n")
    print("4. Access the application:")
    print("   http://localhost:5000\n")
    print("5. Read the documentation:")
    print("   Start with docs/01-getting-started.md\n")

def main():
    """Main setup function"""
    print_header("DevOps Learning Project - Environment Setup")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}\n")
    
    # Check prerequisites
    prereq_results = check_prerequisites()
    
    required = ['Python', 'Git', 'Docker']
    missing_required = [name for name in required if not prereq_results.get(name, False)]
    
    if missing_required:
        print(f"\n❌ Missing required tools: {', '.join(missing_required)}")
        print("Please install them before continuing.")
        sys.exit(1)
    
    # Setup steps
    steps = [
        ("Create Virtual Environment", create_virtual_environment),
        ("Install Dependencies", install_dependencies),
        ("Create Directories", create_directories),
        ("Setup Git Hooks", setup_git_hooks),
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print(f"\n❌ Setup failed at: {step_name}")
            sys.exit(1)
    
    # Display next steps
    display_next_steps()

if __name__ == '__main__':
    main()
