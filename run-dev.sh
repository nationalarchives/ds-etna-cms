#!/bin/bash

poetry run python /app/manage.py makemigrations
# poetry run python /app/manage.py squashmigrations app.articles
poetry run python /app/manage.py migrate --run-syncdb
poetry run python /app/manage.py createsuperuser --no-input
poetry run python /app/manage.py runserver 0.0.0.0:8080