# tell Vercel what commands to run
#!/bin/bash

# Exit the script on any command with non-zero status
set -e

# Build the project
echo "Building the project..."

# pip is available and install dependencies
python3.9 -m pip install -r requirements.txt

# makemigrtions and migrate
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# collect static files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
