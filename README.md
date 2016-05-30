# MacDash

### Beginning steps for running with PostgreSQL on OSX
Download Postgres.app for OSX from http://postgresapp.com
Follow the setup instructions that page to add postgres to your $PATH.

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

## Custom Settings
Create your own custom settings file
```
cp example_custom_settings.py custom_settings.py
```

#### Add Company Name before MacDash
Set the key `MACDASH_BRANDING` in `custom_settings.py`

#### Add JSS Sync Settings
**WARNING: Currently you must set these values otherwise the sync command will not run**
Set the values for the following keys in `custom_settings.py`.
```
JSS_URL
JSS_USER
JSS_PASS
```
These can also be environment variables by including `import os` at the top of `custom_settings.py` and change the following values in `custom_settings.py` to be exactly as follows:
```
JSS_URL = os.environ['JSS_URL']
JSS_USER = os.environ['JSS_USER']
JSS_PASS = os.environ['JSS_PASS']