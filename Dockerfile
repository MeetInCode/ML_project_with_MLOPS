# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port 
EXPOSE $PORT

# Run the application
# This command tells Docker to start the application using Gunicorn, a Python WSGI HTTP server.
# It launches 4 worker processes (--workers=4) to handle requests concurrently.
# The server listens on all network interfaces (0.0.0.0) at the port specified by the $PORT environment variable.
# The application entry point is 'app' inside the 'application' module (application:app).
CMD gunicorn --workers=4 -b 0.0.0.0:$PORT application:app