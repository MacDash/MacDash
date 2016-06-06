#!/usr/bin/env python

from datetime import datetime

from django.conf import settings
from tomorrow import threads

from jss.models import Computer, Site, ComputerApplication
from jss.jss_api import JSSAPISession

casper_client = JSSAPISession(settings.JSS_URL, settings.JSS_USER, settings.JSS_PASSWORD)

def format_jss_computer(jss_computer, sections=list(), no_delete=list()):
    computer_info = jss_computer.get('computer')
    if not sections:
        sections = computer_info.keys()
    # Iterate through all 'sections' of the JSS API computer response and get all keys
    # from from each dictionary to combine all into one dictionary
    formatted_computer_info = dict()
    for section in sections:
        if isinstance(computer_info[section], dict):
            for key, value in computer_info[section].items():
                formatted_computer_info[key] = value
        else:
            formatted_computer_info[section] = computer_info[section]

    # Retrieve field names for a 'Computer' object.
    field_names = [field.name for field in Computer._meta.get_fields()]
    for key, value in formatted_computer_info.copy().items():
        if (key not in field_names or value in ('', None)) and key not in no_delete:
            #Remove values that are None or ''.
            del formatted_computer_info[key]
        elif 'utc' in key:
            # Format date in a python friendly way that can be serialized by Django
            # This only affects dates in the JSS API response that are utc
            formatted_computer_info[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f%z')
    
    return formatted_computer_info

@threads(5)
def update_computer(jss_id, name):
    print('Syncing computer: {}'.format(name))
    request = casper_client.lookup_by_id(jss_id).json()
    
    # Get nested dictionaries from the JSS API response and combine 
    # them all in 'formatted_computer_info'
    jss_computer_sections = ['general', 'purchasing', 'hardware', 'location', 'software', 'extension_attributes']
    included_extra_fields = ['id', 'applications', 'site', 'installed_by_casper', 'extension_attributes']
    jss_computer_info = format_jss_computer(
        request, sections=jss_computer_sections, no_delete=included_extra_fields
    )

    # remove the jss computer id, site and applications details from 'jss_computer_info'. 
    # We'll need them to be separate from the rest of the fields
    jss_computer_id = jss_computer_info.pop('id')
    jss_computer_applications = jss_computer_info.pop('applications')
    jss_site_details = jss_computer_info.pop('site')

    # Get or create a 'Computer' with specified 'computer_id' and set fields 
    # from 'jss_computer_info'
    computer, _ = Computer.objects.get_or_create(computer_id=jss_computer_id)
    for field, val in jss_computer_info.items():
        setattr(computer, field, val)
    computer.save()

    # Get or create a 'Site' if included the JSS API response and add it to 'computer'
    if jss_site_details:
        jss_site, _ = Site.objects.get_or_create(**jss_site_details)
        computer.site = jss_site
        computer.save()

    # Iterate through all applications and get or create a 'ComputerApplication' object
    print('Syncing {} applications for {}'.format(len(jss_computer_applications), name))
    for application in jss_computer_applications:
        app, _ = ComputerApplication.objects.get_or_create(**application)
        computer.applications.add(app)
        computer.save()


def update_all_computers():
    request = casper_client.get_all_computers().json()
    for comp in request['computers']:
        update_computer(comp.get('id'), comp.get('name'))
