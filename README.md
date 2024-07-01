# Kubernetes Deployment and Testing

## Setup

1. **Install Minikube**:

   - Follow the installation guide [here](https://minikube.sigs.k8s.io/docs/start/).

2. **Start Minikube with Docker Driver**:

   ```sh
   minikube start --driver=docker
   ```

3. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Navigate to the Kubernetes manifests directory**:

   ```sh
   cd qa-test/Depolyment
   ```

5. **Apply Kubernetes configurations**:

   ```sh
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
   ```

6. **Get the frontend service URL**:

   ```sh
   minikube service frontend-service --url
   ```

7. **Access the frontend URL** using the output from the above command.

## Automated Testing

1. **Ensure you have `curl` installed**.
2. **Run the test script**:
   ```sh
   ./test_integration.sh
   ```

## Expected Output

- Accessing the frontend URL should display the greeting message fetched from the backend.

## Setup Instructions

## System Health Monitoring Script

```
pip install psutil

```

## Run The Script

python system_health_monitor.py

## Expected Output

CPU Usage:
Memory Usage:
