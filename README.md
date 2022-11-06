Open project in your code editor

Use venv

pip install -r requirements.txt

Create a PostgreSQL database.

Change setting about your information(DB)

In terminal:

python manage.py makemigrations main
python manage.py migrate main
python manage.py migrate
python manage.py createsuperuser, create a superuser.
python manage.py runserver.
 
 
I did 2 parts of the test. The first app with registration and authentication.
The second python code, which takes information from csv and xml files. Which we need. (in 'scraping_document.py')

