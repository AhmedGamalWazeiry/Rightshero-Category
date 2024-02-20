#!/bin/bash

. $VENV_PATH/bin/activate

poetry run python manage.py makemigrations

poetry run python manage.py migrate

poetry run python manage.py collectstatic  --noinput --clear

echo "Creating superuser $DJANGO_SUPERUSER_EMAIL with username $DJANGO_SUPERUSER_USERNAME"

poetry run python manage.py createsuperuser --noinput

poetry run python manage.py initcategory

exec "$@"
