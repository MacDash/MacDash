# MacDash

**ATTENTION: MACDASH IS IN EARLY DEVELOPMENT, USE AT YOUR OWN RISK**

![MacDash Dashboard](https://github.com/cshepp1211/MacDash/blob/master/Screenshots/MacDash_Dashboard.jpg)

## Run with PostgreSQL in a Virtual Environment on OSX

### 1. Install Xcode
```
xcode-select --install
```
### 2. Install Homebrew
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### 3. Insert HomeBrew Directory at the top of the PATH environment variable.
```
sudo nano ~/.bash_profile
```
Then add the following line:
``` 
export PATH=/usr/local/bin:$PATH 
```
Restart Terminal to make changes effective
### 4. Install python 3
```
brew install python3
```
Check version - ```python3 --version```

Installing python3 via homebrew also installs:  
  - the updated pip package manager, pip3  
  - the corresponding Setuptools  
  - pyenv which is an alternative to virtualenv  

### 5. Install Postgres
```
brew install postgres
```
### 6. Clone MacDash from the Github repo:
```
git clone https://github.com/MacDash/MacDash.git
```
### 7. Create and start a Virtual Environment
cd to MacDash and entering the following:
```
pyvenv mdvenv
```
(substitute mdvenv for whatever you would like to call the virtual envrionment)
Start the virtual environment by entering:
```
source mdvenv/bin/activate
```
### 8. Install Requirments
Type into terminal:
```
pip3 install -r requirements.txt
```
### 9. Start PostgreSQL and Create a Database
Make sure the Postgres server is running by typing:
```
brew services start postgresql
```
This will allow postgres to start at login, if you don't want it to start at login (background service) then enter in:
```
postgres -D /usr/local/var/postgres
```
To create a DB, in terminal type:
```
createdb macdash
```
(you can substitute macdash for whatever you would like to call your db)
### 10. Create Tables
```
python manage.py migrate
```
### 11. Create a Super User for Django
```
python manage.py createsuperuser
```
  - Enter in Username, or leave blank to use logged in user  
  - Enter in Email Address  
  - Enter in password twice  

### 12. Start the server
  In terminal, enter in:
  ```
  python manage.py runserver
  ```
Open a browser and go to http://127.0.0.1:8000/. Login with the Super User credential you created in step 11
### 13. Create a Custom Setting File
Let's create a custom setting file that will house your JSS credentials as well as a place to give your MacDash a custom name. 
Now would be a good time to make sure to have a user in the JSS with API read privelages.
Stop the server by hitting CONTROL-C and then typing into terminal:
```
cp example_custom_settings.py custom_settings.py
```
Edit the new custom_settings.py and enter your:
  -MacDash Name - The name you give it will preceed the MacDash name ex. ComcoMacDash  
  - JSS URL - FQDN = https://yourjss.com:8443  
  - JSS User - the user that has API read privelages  
  - JSS Password - Password for above user  

### 14. Sync JSS DB to local DB
In terminal, enter in:
```
python manage.py jsssync
```
The Database will begin to sync
### 15. Start server to see results
```
python manage.py runserver
```
If you get an error that the port is already in use, run the following command:
```
sudo lsof -t -i tcp:8000 | xargs kill -9
```
  - Go to Devices > All Devices to see machines  
  - Applications to see Applications

** The custom settings can also be environment variables by including `import os` at the top of `custom_settings.py` and change the following values in `custom_settings.py` to be exactly as follows:
```
JSS_URL = os.environ['JSS_URL']
JSS_USER = os.environ['JSS_USER']
JSS_PASS = os.environ['JSS_PASS']
