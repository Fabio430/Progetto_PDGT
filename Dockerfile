# docker build -t movies-api .
# Per far partire il docker container: docker run -d -p 5000:5000 movies-api
# docker run -dp 5005:5000 -w /app -v "/e/Storage_E/PDGT/2023/Progetto_PDGT:/app" movies-api
# FROM python:3.12
# EXPOSE 5000
# WORKDIR /app
# RUN pip install flask
# COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]



# FROM python:3.12
# EXPOSE 5000
# WORKDIR /app
# COPY ./requirements.txt requirements.txt
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
# COPY . .
# CMD ["flask", "run", "--host", "0.0.0.0"]

# FROM python:3.12
# # Set environment variables for resource limits
# # ENV CPU_LIMIT=0.5
# ENV MEMORY_LIMIT=512M
# # Expose port
# EXPOSE 5000
# # Set working directory
# WORKDIR /app
# # Copy requirements and install dependencies
# COPY ./requirements.txt requirements.txt
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
# # Copy the rest of the application code
# COPY . .
# # Command to run the application with resource limits
# CMD ["sh", "-c", "ulimit -v $MEMORY_LIMIT && python -m flask run --host=0.0.0.0 --port=5000"]
#CMD ["sh", "-c", "memory_limit_in_bytes=$((MEMORY_LIMIT * 1024 * 1024 * 1024)) && ulimit -v $memory_limit_in_bytes && python -m flask run --host=0.0.0.0 --port=5000"]
#CMD ["sh", "-c", "memory_limit_in_bytes=$(echo $MEMORY_LIMIT | sed 's/[^0-9]*//g') && ulimit -v $memory_limit_in_bytes && python -m flask run --host=0.0.0.0 --port=5000"]








FROM python:3.12
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
CMD ["/bin/bash", "docker-entrypoint.sh"]