python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py generate_users 
python manage.py generate_sessions
python manage.py create_admin_user 

gunicorn system.wsgi:application --bind :8000
