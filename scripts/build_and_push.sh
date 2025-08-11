#!/usr/bin/env bash
set -euo pipefail
echo "Building ML image..."
docker build -t devops-mlops-ml:latest ./ml
echo "Building API image..."
docker build -t devops-mlops-api:latest ./app/api
echo "Done. You can push to registry using docker push."
