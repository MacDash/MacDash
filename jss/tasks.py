from datetime import datetime

from django.conf import settings

from jss.models import Computer, Site
from jss.jss_api import JSSAPISession


casper_client = JSSAPISession(settings.JSS_URL, settings.JSS_USER, settings.JSS_PASSWORD)


def update_computers():
    request = casper_client.get_all_computers().json()
    for comp in request['computers']:
        print('Syncing computer: {}'.format(comp.get('name')))
        request = casper_client.lookup_by_id(comp.get('id')).json()
        
        general_details = request['computer']['general']
        del general_details['id']

        field_names = [field.name for field in Computer._meta.get_fields()]
        for key, value in general_details.copy().items():
            if key not in field_names or value in ('', None):
                del general_details[key]
            elif 'utc' in key:
                general_details[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f%z')

        site_details = general_details.pop('site', None)
        if site_details:
            site, created = Site.objects.get_or_create(**site_details)
        else:
            site = None
        computer = Computer.objects.get_or_create(computer_id=comp.get('id'), site=site, **general_details)