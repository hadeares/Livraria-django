web: gunicorn livraria.wsgi:application
heroku ps:scale web=1
python manage.py migrate