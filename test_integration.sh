#!/bin/bash

FRONTEND_URL=$(minikube service frontend-service --url)

RESPONSE=$(curl -s $FRONTEND_URL)

if [[ $RESPONSE == *"Hello from the Backend!"* ]]; then
  echo "Test passed: Greeting message from backend is displayed."
  exit 0
else
  echo "Test failed: Greeting message from backend is not displayed."
  exit 1
fi
