# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local src directory to the container
COPY src/ /app/src

# Install project dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "src/factorial_calculator.py"]

