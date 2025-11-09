#!/usr/bin/env bash
set -e

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn on port \$PORT..."
exec gunicorn approvals.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 2 \
  --log-level info