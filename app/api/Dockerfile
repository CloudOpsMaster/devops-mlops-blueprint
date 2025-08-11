FROM python:3.10-slim
WORKDIR /app
COPY app/api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/api/ ./
ENV PYTHONUNBUFFERED=1
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8080", "--workers", "2"] 
