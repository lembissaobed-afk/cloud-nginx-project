# Cloud Nginx Reverse Proxy Project

A containerized web stack: Nginx as a reverse proxy in front of a Python Flask app served by Gunicorn, orchestrated with Docker Compose.

## Architecture

Client -> Nginx (port 80) -> Flask/Gunicorn (port 5000, internal only)

## Features

- Nginx reverse proxy configuration (nginx/default.conf)
- Flask API with /, /api and /health endpoints
- Gunicorn production server inside a Docker image
- Container health check; Nginx starts only after Flask is healthy

## Project structure

- app/ : Flask app, requirements, Dockerfile
- nginx/ : Nginx configuration
- monitoring/ : system monitoring script (CPU, memory, disk)
- compose.yaml : Docker Compose definition

## Run it

Requirements: Docker with Docker Compose.

    docker compose up --build -d
    docker compose ps
    curl http://localhost
    curl http://localhost/api

Stop it with: docker compose down

## Monitoring script

monitoring/monitor.py logs CPU, memory and disk usage every 5 seconds using psutil:

    pip install psutil
    python3 monitoring/monitor.py

## Roadmap

- [ ] HTTPS (TLS) on Nginx
- [ ] CI with GitHub Actions
- [ ] Deploy to a cloud VM
- [ ] Prometheus and Grafana monitoring

## Author

Obed LEMBISSA MAGNAGNA
