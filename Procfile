release: python manage.py migrate && python manage.py create_superuser_from_env
web: gunicorn amazon.wsgi 