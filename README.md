# Projekt podpor vedu (podporvedu.cz)
=====================================
[PodporVedu][http://damp-ravine-2660.herokuapp.com/]


## Setup project on local development machine

**Prerequsities:**
Installed python, vitualenv and pip

1. Create new enviroment for the project
    $python virtualenv.py podporvedu
2. Activate new env
    $source podporvedu/bin/activate
3. Install django and other dependencies
    $pip install django heroku psycopg2 dj-database-url
4. Clone git repository in folder of your choice
    $git clone https://github.com/mar1221/podporvedu.git
5. Change to project folder
6. Run syncdb (every manage.py command must be called with option --setting pointing to settings_local.py)
    $python manage.py syncdb --settings podporvedu.settings_local
7. Run server
    $python manage.py runserver --settings podporvedu.settings_local

## Deployment on heroku

1. Add and commit changes to your local git repository
    $git add .
    $git commit -m "Name of the commit"
2. (optional) Push to github
    $git push
3. Push to heroku
    $git push heroku master
4. If changes to db has been made sync it
    $heroku run python manage.py syncdb

More info in [heroku docs][https://devcenter.heroku.com/articles/django#commit-to-git]