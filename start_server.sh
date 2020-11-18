python /src/manage.py makemigrations
python /src/manage.py migrate
python /src/manage.py loaddata src/fixtures/initial.json
python /src/manage.py runserver 0.0.0.0:8000