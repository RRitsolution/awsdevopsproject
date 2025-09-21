# Use a lightweight Python 3.9 image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the build dependencies required for mysqlclient
# 'build-base' provides tools like gcc, make, etc.
# 'mariadb-dev' provides the development headers for the database client

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       pkg-config \
       build-essential \
       default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files from the current directory into the container
COPY app.py .

# Set the command to run when the container starts
CMD ["/bin/bash", "-c", "sleep 60 && python app.py"]
