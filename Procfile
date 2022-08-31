release: manage.py migrate
python manage.py collectstatic --noinput
web: gunicorn livraria.wsgi:application --log-file - --log-level debug
