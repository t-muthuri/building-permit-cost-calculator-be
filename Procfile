release: python manage.py migrate
web: gunicorn approvals.wsgi:application --bind 0.0.0.0:$PORT --log-level info