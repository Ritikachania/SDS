# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent .pyc files and ensure logs are output immediately
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container at /app
COPY requirements.txt /app/

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/

# Open port 8000 for serving the Django app
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

