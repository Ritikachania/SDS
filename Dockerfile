# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app/

# Expose the port that the Django application will run on
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
