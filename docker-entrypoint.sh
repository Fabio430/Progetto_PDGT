# Entrypoint script to run database migrations and start the server

# Command to use the sh shell to interpret and execute the commands in the script
#!/bin/sh

flask db upgrade # Apply database migrations

exec gunicorn --bind 0.0.0.0:80 "app:create_app()"