# Dockerfile for surveyhub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies INCLUDING postgresql-client
RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy the wait script and make it executable
COPY wait-for-posgres.sh /wait-for-posgres.sh
RUN chmod +x /wait-for-posgres.sh

# Expose port 8000
EXPOSE 8000