FROM python:3.10-slim
WORKDIR /ml
COPY ml/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ml/ ./
ENTRYPOINT ["python", "train.py"]
