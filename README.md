This repository contains my solution for the Silverfort DevOps technical challenge.

## Overview
The solution includes:
- Python Flask application serving HTTPS content
- Dockerized application
- Kubernetes deployment using Helm
- Service exposed via NodePort
- Self-signed TLS certificate

## Application Output
The application serves a web page with:
- Client IP address
- Container (Pod) name
- Current temperature in Tel-Aviv (using Open-Meteo API)

## How to Run

### Build Docker Image
```bash
eval $(minikube docker-env)
docker build -t silverfort-app:1.0 .

