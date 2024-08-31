# Use a base image with Python
FROM python:3.11-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Update pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "student_management_system.wsgi:application"]
