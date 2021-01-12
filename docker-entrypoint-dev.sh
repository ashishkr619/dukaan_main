#!/bin/bash
# This script must not be used for production.

set -e

bash scripts/wait-for-it.sh $DATABASE_HOST $DATABASE_PORT

echo $(date -u) "- Migrating"
python manage.py makemigrations
python manage.py migrate

echo $(date -u) "- Creating admin user"
python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model();User.objects.filter(phone_number='1111').delete();User.objects.create_superuser('1111','7879')"

echo $(date -u) "- Running the server"
gunicorn dukaan_service.wsgi --config dukaan_service/gunicorn_conf.py --workers 2 --timeout 120 --reload
