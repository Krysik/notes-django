web: rm -r staticfiles
web: python manage.py collectstatic
web: gunicorn notes.wsgi --log-file -