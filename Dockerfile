# Dockerfile to containerize the application
# Use Python 3.12 as the base image from the Docker Hub registry
FROM python:3.12
# Set the working directory inside the container to /app
WORKDIR /app
# Copy the requirements.txt file from the current directory on the host to the /app directory in the container
COPY ./requirements.txt requirements.txt
# Install the Python dependencies specified in requirements.txt
# --no-cache-dir: Do not store the cache of the packages to save space
# --upgrade: Upgrade all specified packages to the newest available version
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Copy everything from the current directory on the host to the /app directory in the container
COPY . .
# Set the default command to execute when the container starts
# Here it runs a shell script named 'docker-entrypoint.sh' located in the /app directory
CMD ["/bin/bash", "docker-entrypoint.sh"]