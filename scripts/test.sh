#!/usr/bin/env bash
set -e

docker-compose build
docker-compose run -w /app app mypy ./mysite
docker-compose run app python manage.py test polls