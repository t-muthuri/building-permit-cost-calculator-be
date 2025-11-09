#!/bin/bash
set -e  # Exit on any error

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server
exec "$@"