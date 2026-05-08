# HiveBox

A lightweight Flask API that exposes application version information, containerized with Docker and deployable to Kubernetes.

## Project Structure

```
HiveBox/
├── app.py              # Flask application entry point
├── app_version.py      # Version constant and helper
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container image definition
├── manifests/
│   ├── deployment.yaml # Kubernetes Deployment
│   └── svc.yaml        # Kubernetes Service (LoadBalancer)
└── testfox.py          # Tests
```

## API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| GET    | `/version` | Returns the app version  |

Example response:
```
Version: 0.0.1
```

## Local Development

### Prerequisites

- Python 3.9+

### Setup

```powershell
# Create virtual environment
py -3 -m venv .venv

# Activate it
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run

```powershell
flask --app app run
```

The app will be available at `http://127.0.0.1:5000`.

## Docker

### Build

```bash
docker build -t hivebox .
```

### Run

```bash
docker run -p 5000:5000 hivebox
```

## Kubernetes

Apply the manifests to deploy to a cluster:

```bash
kubectl create namespace hivebox
kubectl apply -f manifests/
```

The Service exposes port 80 (mapped to container port 5000) via a LoadBalancer.
