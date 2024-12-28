# Kubernetes Automation Script

## Overview

This project provides a set of scripts to automate operations on a bare Kubernetes cluster, including connecting to the cluster, installing Helm and KEDA, creating deployments with event-driven scaling, and retrieving health status for a given deployment ID.

## Project Structure

k8s-automation-script/
├── config/
│   └── config.yaml
├── manifests/
│   ├── deployment.yaml
│   ├── hpa.yaml
│   └── service.yaml
├── src/
│   ├── connect_cluster.py
│   ├── create_deployment.py
│   ├── get_health_status.py
│   └── install_tools.py
├── .gitignore
├── deploy.yaml
├── requirements.txt
└── setup.py

## Prerequisites

- Python 3.x
- `kubectl` installed and configured
- `helm` installed

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Aditya-OO7/assignment01.git
    cd assignment01/k8s_automation_script
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Install the package:
    ```sh
    pip install -e .
    ```

## Usage

### Connect to Cluster
Connect a `kubectl` client to the provided cluster:
```sh
connect-cluster <kubeconfig-path>
```

### Install Helm
Install Helm on the Kubernetes cluster:
```sh
install-helm
```

### Install KEDA
Use Helm to install KEDA on the Kubernetes cluster:
```sh
install-keda
```

### Create Deployment
Create a deployment using the provided configuration file:
```sh
create-deployment <config-path>
```

#### Example `config.yaml`
```yaml
deployment: deployment.yaml
service: service.yaml
hpa: hpa.yaml
```

### Get Health Status
Retrieve the health status of a given deployment ID:
```sh
get-health-status <deployment-id>
```

## Configuration Files

### Example `deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-deployment
  labels:
    app: example
spec:
  replicas: 1
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
      - name: example-container
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
```

### Example `service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

### Example `hpa.yaml`
```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: example-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: example-deployment
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```
