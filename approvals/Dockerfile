FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
        default-libmysqlclient-dev \
        build-essential \
        python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Create a virtual environment and install Python dependencies
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Verify gunicorn installation
RUN /opt/venv/bin/pip show gunicorn

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"

# Default command
CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "approvals.wsgi:application"]
