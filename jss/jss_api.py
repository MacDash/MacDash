import requests
import base64

class JSSAPISession(object):

    def __init__(self, jss_url, username, password):
        auth = base64.b64encode(
            '{username}:{password}'.format(
                username=username,
                password=password,
            ).encode('ascii')
        ).decode('utf-8')
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic {auth}'.format(auth=auth)
        }
        self.api_session = requests.Session()
        self.api_session.headers.update(headers)
        self.jss_url = '{base}/JSSResource'.format(base=jss_url.rstrip('/'))

    def run_request(self, endpoint_url):
        request_url = '{api_base}{endpoint_url}'.format(
            api_base=self.jss_url,
            endpoint_url=endpoint_url,
        )

        api_request = self.api_session.get(request_url)
        return api_request

    def lookup_by_serial(self, serial_number, session=None):
        """
        Get computer by serial. Creates session object if not provided.
        Arguments:
            serial_number (str): Mac serial number
            session (requests.Session) - optional: Requests Session object
        Returns:
            Requests Response object
        """

        computer_url = '/computers/serialnumber/{serial}'.format(
            serial=serial_number
        )
        return self.run_request(computer_url)


    def lookup_by_id(self, comp_id):
        computer_url = '/computers/id/{id}'.format(id=comp_id)
        try:
            return self.run_request(computer_url)
        except simplejson.JSONDecodeError:
            print('error retrieving {id}'.format(id=comp_id))

    def get_all_computers(self):
        return self.run_request('/computers')