#!/usr/bin/env python3
"""
Bob Application - Simple Flask App for Demo
Demonstrates automated deployment via Jenkins webhook
"""

from flask import Flask, jsonify, request
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Configuration
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'production')
BUILD_NUMBER = os.getenv('BUILD_NUMBER', 'unknown')

@app.route('/')
def home():
    """Home endpoint - returns deployment information"""
    return jsonify({
        'message': '🤖 Bob Deployment Pipeline - Working!',
        'status': 'success',
        'version': APP_VERSION,
        'environment': ENVIRONMENT,
        'build_number': BUILD_NUMBER,
        'hostname': socket.gethostname(),
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        'status': 'healthy',
        'version': APP_VERSION,
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/ready')
def ready():
    """Readiness probe endpoint"""
    return jsonify({
        'status': 'ready',
        'version': APP_VERSION
    }), 200

@app.route('/info')
def info():
    """Application information endpoint"""
    return jsonify({
        'application': 'Bob Deployment App',
        'version': APP_VERSION,
        'environment': ENVIRONMENT,
        'build_number': BUILD_NUMBER,
        'hostname': socket.gethostname(),
        'python_version': os.sys.version,
        'endpoints': {
            'home': '/',
            'health': '/health',
            'ready': '/ready',
            'info': '/info',
            'webhook-test': '/webhook-test'
        }
    })

@app.route('/webhook-test')
def webhook_test():
    """Test endpoint to verify webhook deployment"""
    return jsonify({
        'message': '✅ Webhook deployment successful!',
        'deployed_at': datetime.utcnow().isoformat(),
        'build_number': BUILD_NUMBER,
        'note': 'This deployment was triggered by GitHub webhook'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested endpoint does not exist',
        'available_endpoints': [
            '/',
            '/health',
            '/ready',
            '/info',
            '/webhook-test'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    print('=' * 60)
    print(f'🤖 Bob Application v{APP_VERSION}')
    print(f'Environment: {ENVIRONMENT}')
    print(f'Build: {BUILD_NUMBER}')
    print('=' * 60)
    
    # Run on all interfaces, port 8080
    app.run(host='0.0.0.0', port=8080, debug=False)

# Made with Bob
