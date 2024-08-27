# CONTRIBUTING

## How to run the Dockerfile locally

docker run -dp 5000:5000 -w /app -v "/e/Storage_E/PDGT/2023/Progetto_PDGT:/app" movies-api sh -c "flask run --host 0.0.0.0"


## Indirizzo dell'app fino a che si è nella fase di sviluppo e non si è ancora fatto il deployment dell'app su un servizio online
http://127.0.0.1:5000/



## REQUIREMENTS.TXT
pip install -r requirements.txt






## Per fare la build del container
This command tells Docker to:
- Look for a Dockerfile in the current directory (.).
- Use the instructions in that Dockerfile to build an image.
- Tag the resulting image with the name movies-api, the -t flag allows you to tag the image with a name and optionally a version.

docker build -t movies-api .
## Per far partire il docker container
This command tells Docker to:
- Start a container from the movies-api image.
- Run the container in the background (detached mode), -d.
- Map port 5000 on your local machine to port 5000 inside the container, -p 5000(local machine):5000(container), -p host_port:container_port
- The application running in the container will be accessible on http://localhost:5000 if it is listening on port 5000 inside the container.

docker run -d -p 5000:5000 movies-api
## altro comando
docker run -dp 5005:5000 -w /app -v "/e/Storage_E/PDGT/2023/Progetto_PDGT:/app" movies-api

## DOCKERFILE
FROM python:3.12
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]



FROM python:3.12
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


FROM python:3.12
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]


## API secret key
the secret key set here, "fabio", is not very safe
Instead you should generate a long and random secret key using something like:
import secrets

def generate_secret_key(length):
    return secrets.token_urlsafe(length)

""" Generate a secret key with a specified length (e.g., 32 bytes) """
secret_key = generate_secret_key(32)
print("Generated Secret Key:", secret_key)

## Quando non si usa il database migration, il comando per creare il database quando si avvia l'app è il seguente
with app.app_context():
    db.create_all()