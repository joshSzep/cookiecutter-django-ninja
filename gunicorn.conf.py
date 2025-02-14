import multiprocessing

# Worker configuration
workers = (multiprocessing.cpu_count() * 2) + 1  # Formula: (2 x CPU cores) + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000

# Process management
max_requests = 1000  # Prevent memory leaks
max_requests_jitter = 100  # Add randomness to prevent all workers restarting at once

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Socket configuration
bind = "0.0.0.0:8000"

# Environment
env = {
    "DJANGO_SETTINGS_MODULE": "backend.project.settings",
}
