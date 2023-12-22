python3.9 manage.py makemigrations
#python3.9 manage.py migrate --fake useradmin zero
python3.9 manage.py migrate useradmin
python3.9 manage.py runserver