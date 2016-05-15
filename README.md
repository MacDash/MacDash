# MacDash

### Beginning steps for running with PostgreSQL on OSX
Download Postgres.app for OSX from http://postgresapp.com

## Install Requirements
```
pip install -r requirements.txt
```

## Create the SQLite3 Database and Migrate to 
Create Tables(temporary)
```
python manage.py migrate
```

## Create a super user
```
python manage.py createsuperuser
```

## Run the built in server
```
python manage.py runserver
```