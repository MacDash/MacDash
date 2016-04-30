  # run.py

from flask import Flask, render_template
import requests
import json

application = Flask(__name__)

@application.route('/')
def homepage():
  headers = {
    'authorization': "Basic YXBpX3JlYWQ6bWs5Q3E0SFZmIQ==",
    'accept': "application/json",
  }

  r1 = requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/1',
      headers=headers)
  r2 = requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/183',
      headers=headers)
  r3= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/19',
      headers=headers)
  r4= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/196',
      headers=headers)
  r5= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/195',
      headers=headers)
  r6= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/mobiledevicegroups/id/5',
      headers=headers)
  r7= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/115',
      headers=headers)
  r8= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/134',
      headers=headers)
  r9= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/119',
      headers=headers)
  r10= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/136',
      headers=headers)
  r11= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/135',
      headers=headers)
  r12= requests.get(
      'https://jss01.fnal.gov:8443/JSSResource/computergroups/id/153',
      headers=headers)


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
