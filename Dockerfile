# Use the official Python base image from the Docker Hub
FROM python:3.9-slim

# Install necessary dependencies and Microsoft ODBC Driver for SQL Server
RUN apt-get update && \
    apt-get install -y \
    gnupg \
    curl \
    apt-transport-https \
    ca-certificates \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
EXPOSE 8000

# Define environment variable for the application (optional)
ENV PYTHONUNBUFFERED=1

# Run your Python application (update with the correct entry point, e.g., app.py)
CMD ["python", "main.py"]
