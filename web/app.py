# run.py

from flask import Flask, render_template
import requests
import json
from base64 import b64encode

app = Flask(__name__)
app.config.from_object('config')

credentials = '{username}:{password}'.format(
  username=app.config['JSS_USERNAME'],
  password=app.config['JSS_PASSWORD'])

authorization = 'Basic {auth}'.format(auth=b64encode(credentials.encode('ascii')))

def jss_request(endpoint):
    headers = {
        'authorization': authorization,
        'accept': "application/json",
    }
    jss_request_url = '{base}{endpoint}'.format(
        base=app.config['JSS_RESOURCE_BASE_URL'].strip('/'),
        endpoint=endpoint)
    r = requests.get(jss_request_url)
    return r


@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
