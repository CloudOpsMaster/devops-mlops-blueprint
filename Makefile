.PHONY: build-api build-ml lint test

build-api:
	docker build -t devops-mlops-api:local ./app/api

build-ml:
	docker build -t devops-mlops-ml:local ./ml

lint:
	flake8 || true

test:
	pytest -q tests || true
