# Demo steps (local)

1. Build ML image:
   docker build -t devops-mlops-ml:local ./ml

2. Train model:
   docker run --rm devops-mlops-ml:local

3. Build API:
   docker build -t devops-mlops-api:local ./app/api

4. Run API:
   docker run -p 8080:8080 devops-mlops-api:local

5. Test inference:
   curl -X POST -H 'Content-Type: application/json' --data '{ "input": [5.1, 3.5, 1.4, 0.2] }' http://localhost:8080/predict
