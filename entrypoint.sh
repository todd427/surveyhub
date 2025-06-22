#!/bin/bash
set -e

# Run database migrations
echo "Applying database migrations..."
python manage.py migrate --settings=surveyhub.settings.prod

# (Optional) Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=surveyhub.settings.prod

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn surveyhub.wsgi:application --bind 0.0.0.0:8000
