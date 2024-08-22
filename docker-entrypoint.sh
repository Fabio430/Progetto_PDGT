# Entrypoint script to run database migrations and start the server

#!/bin/sh

flask db upgrade # Apply database migrations

exec gunicorn --bind 0.0.0.0:80 "app:create_app()"