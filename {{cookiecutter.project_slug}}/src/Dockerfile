FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    gettext \
    libpq-dev \
    postgresql \
    postgresql-contrib

COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
COPY . .

EXPOSE 8000

