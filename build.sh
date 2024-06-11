#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Build the project
echo "Building the project..."

# Ensure Python and pip are available
echo "Ensuring pip is available..."
python3.9 -m ensurepip --upgrade || true
python3.9 -m pip install --upgrade pip

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3.9 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install wheel
pip install -r requirements.txt

# Make Migrations and Migrate
echo "Making Migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect Static Files
echo "Collecting Static files..."
python manage.py collectstatic --noinput --clear
