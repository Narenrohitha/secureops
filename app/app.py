"""
SecureOps Platform - Python Flask Web Application
A production-grade DevSecOps dashboard with real metrics, health endpoints,
and Prometheus instrumentation.
"""

import os
import time
import socket
import platform
import psutil
from datetime import datetime
from flask import Flask, render_template, jsonify, request
from prometheus_client import (
    Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
)
import logging

# ─── App Setup ──────────────────────────────────────────────────────────────
app = Flask(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV     = os.getenv("APP_ENV", "production")
START_TIME  = time.time()

# ─── Prometheus Metrics ───────────────────────────────────────────────────
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

ACTIVE_USERS = Gauge(
    'active_users_total',
    'Number of active users'
)

DEPLOYMENT_INFO = Gauge(
    'deployment_info',
    'Deployment information',
    ['version', 'environment']
)
DEPLOYMENT_INFO.labels(version=APP_VERSION, environment=APP_ENV).set(1)

# ─── Middleware ───────────────────────────────────────────────────────────
@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - request.start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown',
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(endpoint=request.endpoint or 'unknown').observe(duration)
    logger.info(f"{request.method} {request.path} → {response.status_code} ({duration:.3f}s)")
    return response

# ─── Routes ───────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html',
                           version=APP_VERSION,
                           environment=APP_ENV)

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route('/ready')
def ready():
    """Kubernetes readiness probe"""
    return jsonify({"status": "ready"}), 200

@app.route('/api/system')
def system_info():
    cpu    = psutil.cpu_percent(interval=0.1)
    mem    = psutil.virtual_memory()
    disk   = psutil.disk_usage('/')
    uptime = round(time.time() - START_TIME, 2)

    ACTIVE_USERS.set(cpu / 10)   # simulated metric

    return jsonify({
        "hostname":     socket.gethostname(),
        "platform":     platform.system(),
        "python":       platform.python_version(),
        "cpu_percent":  cpu,
        "memory": {
            "total_gb":    round(mem.total / (1024**3), 2),
            "used_gb":     round(mem.used  / (1024**3), 2),
            "percent":     mem.percent
        },
        "disk": {
            "total_gb":    round(disk.total / (1024**3), 2),
            "used_gb":     round(disk.used  / (1024**3), 2),
            "percent":     disk.percent
        },
        "uptime_seconds": uptime,
        "version":     APP_VERSION,
        "environment": APP_ENV
    })

@app.route('/api/pipeline')
def pipeline_status():
    """Mock CI/CD pipeline stages for dashboard"""
    return jsonify({
        "stages": [
            {"name": "Code Commit",      "status": "success", "duration": "2s"},
            {"name": "SonarQube Scan",   "status": "success", "duration": "45s"},
            {"name": "Trivy FS Scan",    "status": "success", "duration": "12s"},
            {"name": "Docker Build",     "status": "success", "duration": "38s"},
            {"name": "Trivy Image Scan", "status": "success", "duration": "20s"},
            {"name": "Push to ECR",      "status": "success", "duration": "8s"},
            {"name": "ArgoCD Sync",      "status": "running", "duration": "..."},
            {"name": "Health Check",     "status": "pending", "duration": "-"},
        ],
        "build_number": os.getenv("BUILD_NUMBER", "42"),
        "branch":       "main",
        "commit":       "a3f91bc",
        "triggered_by": "push"
    })

@app.route('/api/security')
def security_status():
    """Mock security scan results"""
    return jsonify({
        "trivy": {
            "critical": 0,
            "high":     2,
            "medium":   5,
            "low":      12,
            "status":   "passed"
        },
        "sonarqube": {
            "bugs":              0,
            "vulnerabilities":   0,
            "code_smells":       3,
            "coverage":          "82%",
            "quality_gate":      "passed"
        },
        "wazuh": {
            "alerts_24h":   4,
            "critical":     0,
            "high":         1,
            "status":       "monitoring"
        }
    })

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# ─── Error Handlers ───────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "not found", "path": request.path}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "internal server error"}), 500

# ─── Entry Point ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    debug = APP_ENV != "production"
    logger.info(f"Starting SecureOps v{APP_VERSION} on port {port} [{APP_ENV}]")
    app.run(host='0.0.0.0', port=port, debug=debug)
