"""
Unit tests for the Flask application
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app

@pytest.fixture
def app():
    """Create application for testing"""
    flask_app.config['TESTING'] = True
    return flask_app

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

def test_home(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_ready(client):
    """Test readiness endpoint"""
    response = client.get('/ready')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ready'

def test_metrics(client):
    """Test metrics endpoint"""
    response = client.get('/metrics')
    assert response.status_code == 200

def test_info(client):
    """Test info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'version' in data
    assert 'app' in data

def test_get_tasks(client):
    """Test getting all tasks"""
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)

def test_create_task(client):
    """Test creating a task"""
    new_task = {'title': 'Test Task', 'completed': False}
    response = client.post('/api/tasks', json=new_task)
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Task'
    assert 'id' in data

def test_create_task_missing_title(client):
    """Test creating a task without title"""
    response = client.post('/api/tasks', json={})
    assert response.status_code == 400

def test_get_task(client):
    """Test getting a specific task"""
    response = client.get('/api/tasks/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_get_nonexistent_task(client):
    """Test getting a nonexistent task"""
    response = client.get('/api/tasks/9999')
    assert response.status_code == 404

def test_update_task(client):
    """Test updating a task"""
    update_data = {'title': 'Updated Task', 'completed': True}
    response = client.put('/api/tasks/1', json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Updated Task'
    assert data['completed'] == True

def test_404(client):
    """Test 404 error handler"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
