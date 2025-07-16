release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py create_superuser_from_env --skip-if-exists
web: gunicorn amazon.wsgi