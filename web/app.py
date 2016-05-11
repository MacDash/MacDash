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

authorization = 'Basic {auth}'.format(auth=b64encode(credentials))

def jss_request(endpoint):
    headers = {
        'authorization': authorization,
        'accept': "application/json",
    }
    jss_request_url = '{base}{endpoint}'.format(
        base=app.config['JSS_RESOURCE_BASE_URL'], endpoint=endpoint)
    r = requests.get(jss_request_url)
    return r
    

@application.route('/')
def homepage():


    r1 = jss_request('computergroups/id/1')
    r2 = jss_request('/computergroups/id/183')
    r3 = jss_request('/computergroups/id/19')
    r4 = jss_request('/computergroups/id/196')
    r5 = jss_request('/computergroups/id/195')
    r6 = jss_request('/mobiledevicegroups/id/5')
    r7 = jss_request('/computergroups/id/115')
    r8 = jss_request('/computergroups/id/134')
    r9 = jss_request('/computergroups/id/119')
    r10 = jss_request('/computergroups/id/136')
    r11 = jss_request('/computergroups/id/135')
    r12 = jss_request('/computergroups/id/153')


  return render_template('index.html', allmanaged=len(json.loads(r1.text)['computer_group']['computers']) ,
                                       ccdmanaged=json.loads(r2.text)['computer_group']['computers'] ,
                                       admanaged=json.loads(r3.text)['computer_group']['computers']  ,
                                       manageddesktops=json.loads(r4.text)['computer_group']['computers'] ,
                                       managedlaptops=json.loads(r5.text)['computer_group']['computers'] ,
                                       manageddevices=json.loads(r6.text)['mobile_device_group']['mobile_devices'] ,
                                       mavericksinstalled=json.loads(r7.text)['computer_group']['computers'] ,
                                       yosemiteinstalled=json.loads(r8.text)['computer_group']['computers'] ,
                                       elcapinstalled=json.loads(r9.text)['computer_group']['computers'] ,
                                       lastchecktwenty=json.loads(r10.text)['computer_group']['computers'] ,
                                       lastcheckfortyfive=json.loads(r11.text)['computer_group']['computers'] ,
                                       lastcheckninety=json.loads(r12.text)['computer_group']['computers'])
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
