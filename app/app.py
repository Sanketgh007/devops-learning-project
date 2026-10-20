"""
Simple Flask Application for DevOps Learning
Includes health checks, metrics endpoint, and basic REST API
"""

from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total app requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

# In-memory data store for demo
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Learn Kubernetes", "completed": False},
    {"id": 3, "title": "Setup CI/CD", "completed": False}
]

# Middleware to track metrics
@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(request, 'start_time'):
        latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            status=response.status_code
        ).inc()
    return response

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to DevOps Learning App!",
        "version": "1.0.0",
        "endpoints": {
            "/": "This message",
            "/health": "Health check",
            "/metrics": "Prometheus metrics",
            "/api/tasks": "Task management API",
            "/api/info": "Application info"
        }
    })

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        "status": "healthy",
        "timestamp": time.time()
    }), 200

@app.route('/ready')
def ready():
    """Readiness check endpoint"""
    # Add actual readiness checks here (DB connection, etc.)
    return jsonify({
        "status": "ready",
        "timestamp": time.time()
    }), 200

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/api/info')
def info():
    """Application information"""
    return jsonify({
        "app": "DevOps Learning App",
        "version": "1.0.0",
        "python_version": os.sys.version,
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "hostname": os.getenv('HOSTNAME', 'localhost')
    })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({"tasks": tasks})

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": max([t['id'] for t in tasks]) + 1 if tasks else 1,
        "title": data['title'],
        "completed": data.get('completed', False)
    }
    tasks.append(new_task)
    logger.info(f"Created task: {new_task}")
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])
    logger.info(f"Updated task: {task}")
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    logger.info(f"Deleted task ID: {task_id}")
    return jsonify({"message": "Task deleted"}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting DevOps Learning App on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
