"""This file contains the gunicorn configuration required for the API Server."""

from multiprocessing import cpu_count

bind = "0.0.0.0:4003"

# Worker Options
worker_class = "uvicorn.workers.UvicornWorker"
workers = cpu_count() + 1

# Timeout Options
timeout = 300
graceful_timeout = 300

# Other Options
keepalive = 5
