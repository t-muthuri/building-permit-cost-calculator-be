#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Build the project
echo "Building the project..."

# Make pip available and install dependencies
python3.9 -m ensurepip --upgrade || true
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Make Migrations and Migrate
echo "Make Migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect Static Files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
