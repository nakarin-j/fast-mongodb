FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install -r requirements.txt

ENV WORKERS_PER_CORE 2

COPY . /app