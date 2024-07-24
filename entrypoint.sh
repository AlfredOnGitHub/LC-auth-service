#!/bin/sh

echo "Applying database migrations"
python manage.py migrate

echo "Starting server"
exec gunicorn org_service.wsgi:application --bind 0.0.0.0:8000

