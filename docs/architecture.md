# Architecture

Simple diagram (text):

Developer -> GitHub Actions -> Container Registry -> Kubernetes (inference API)
                           -> Terraform -> Cloud infra
MLflow server -> model registry
Prometheus/Grafana for metrics.
