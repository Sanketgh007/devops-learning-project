#!/usr/bin/env python3
"""
Health check script for monitoring application status
Can be used in CI/CD pipelines or monitoring systems
"""

import requests
import sys
import time
import argparse

def check_health(url, timeout=5, retries=3):
    """
    Check if the application is healthy
    
    Args:
        url: Base URL of the application
        timeout: Request timeout in seconds
        retries: Number of retries
    
    Returns:
        bool: True if healthy, False otherwise
    """
    health_url = f"{url}/health"
    
    for attempt in range(retries):
        try:
            response = requests.get(health_url, timeout=timeout)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'healthy':
                    print(f"✅ Application is healthy: {health_url}")
                    return True
                else:
                    print(f"⚠️  Application returned unexpected status: {data}")
            else:
                print(f"❌ Health check failed with status code: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Health check failed (attempt {attempt + 1}/{retries}): {str(e)}")
            if attempt < retries - 1:
                time.sleep(2)
    
    return False

def check_readiness(url, timeout=5):
    """Check if the application is ready to serve traffic"""
    ready_url = f"{url}/ready"
    
    try:
        response = requests.get(ready_url, timeout=timeout)
        if response.status_code == 200:
            print(f"✅ Application is ready: {ready_url}")
            return True
        else:
            print(f"❌ Readiness check failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Readiness check failed: {str(e)}")
    
    return False

def check_metrics(url, timeout=5):
    """Check if metrics endpoint is accessible"""
    metrics_url = f"{url}/metrics"
    
    try:
        response = requests.get(metrics_url, timeout=timeout)
        if response.status_code == 200:
            print(f"✅ Metrics endpoint is accessible: {metrics_url}")
            return True
        else:
            print(f"❌ Metrics check failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Metrics check failed: {str(e)}")
    
    return False

def check_api(url, timeout=5):
    """Check if API endpoints are working"""
    api_url = f"{url}/api/tasks"
    
    try:
        response = requests.get(api_url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API is working: {api_url}")
            print(f"   Tasks count: {len(data.get('tasks', []))}")
            return True
        else:
            print(f"❌ API check failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ API check failed: {str(e)}")
    
    return False

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Health check for DevOps Learning App")
    parser.add_argument('--url', default='http://localhost:5000', help='Application URL')
    parser.add_argument('--timeout', type=int, default=5, help='Request timeout')
    parser.add_argument('--retries', type=int, default=3, help='Number of retries')
    parser.add_argument('--full', action='store_true', help='Run all checks')
    
    args = parser.parse_args()
    
    print(f"\n🔍 Running health checks for: {args.url}\n")
    
    checks = [
        ("Health", lambda: check_health(args.url, args.timeout, args.retries))
    ]
    
    if args.full:
        checks.extend([
            ("Readiness", lambda: check_readiness(args.url, args.timeout)),
            ("Metrics", lambda: check_metrics(args.url, args.timeout)),
            ("API", lambda: check_api(args.url, args.timeout))
        ])
    
    results = []
    for check_name, check_func in checks:
        print(f"--- {check_name} Check ---")
        result = check_func()
        results.append(result)
        print()
    
    if all(results):
        print("✅ All checks passed!")
        sys.exit(0)
    else:
        print("❌ Some checks failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()
