# Dockerfile for surveyhub
# Use official Python image
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . .

# Collect static files (can also do this in CI or as a startup script)
RUN python manage.py collectstatic --noinput --settings=surveyhub.settings.prod

# Set default environment (can be overridden by Railway/your cloud)
ENV DJANGO_SETTINGS_MODULE=surveyhub.settings.prod

EXPOSE 8000
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Start Gunicorn web server
CMD ["./entrypoint.sh"]
