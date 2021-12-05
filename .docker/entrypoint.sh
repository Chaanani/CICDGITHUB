#!/bin/bash

cd /opt/app

touch ./logs/uwsgi.log
touch ./logs/debug.log

chown www-data:www-data ./logs/uwsgi.log
chown www-data:www-data ./logs/debug.log

if [ "$DB_HOST" = "" ] || [ "$DB_HOST" = "localhost" ]
then
  touch db.sqlite3
  chown www-data:www-data ../app
  chown www-data:www-data db.sqlite3
  chmod 667 db.sqlite3
fi

export DJANGO_SETTINGS_MODULE=todo_backend.settings

ADMIN_USER=${ADMIN_USER:-"admin"}
ADMIN_PASS=${ADMIN_PASS:-"admin"}
ADMIN_EMAIL=${ADMIN_PASS:-"admin@example.com"}

python manage.py migrate --noinput
python manage.py ensure_one_user_exists --username="$ADMIN_USER" --email="$ADMIN_EMAIL" --password="$ADMIN_PASS"
python manage.py collectstatic --noinput

declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env

exec uwsgi --ini .docker/todo_backend.ini
