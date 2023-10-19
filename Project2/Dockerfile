# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to specify Flask's run host
ENV FLASK_RUN_HOST=0.0.0.0

# Make port 12345 available to the world outside this container
EXPOSE 12345

# Run api.py when the container launches
CMD ["python", "api.py"]
