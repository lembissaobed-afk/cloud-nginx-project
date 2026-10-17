# Cloud Nginx Reverse Proxy Project

![CI](https://github.com/lembissaobed-afk/cloud-nginx-project/actions/workflows/ci.yml/badge.svg)

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
    curl -k https://localhost
    curl -k https://localhost/api

Stop it with: docker compose down

## Monitoring script

monitoring/monitor.py logs CPU, memory and disk usage every 5 seconds using psutil:

    pip install psutil
    python3 monitoring/monitor.py

## Roadmap

- [x] HTTPS (self-signed TLS) on Nginx
- [ ] CI with GitHub Actions
- [ ] Deploy to a cloud VM
- [ ] Prometheus and Grafana monitoring

## Author

Obed LEMBISSA MAGNAGNA

## HTTPS certificate (run once before the first start)

The certificate and key are not stored in the repository. Generate a self-signed pair:

    mkdir -p nginx/certs
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
      -keyout nginx/certs/server.key -out nginx/certs/server.crt \
      -subj "/CN=localhost"

Nginx redirects HTTP (80) to HTTPS (443). Browsers warn about self-signed certificates, which is expected. Use `curl -k` to skip verification when testing.
