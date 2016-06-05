from django.shortcuts import render, get_object_or_404
# from django.conf import settings
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext

from jss.models import Computer, ComputerApplication


def _format_device(computer):
    comp_dict = computer.__dict__
    if computer.last_contact_time_utc:
        comp_dict['last_contact_time_utc'] = computer.last_contact_time_utc.strftime('%Y-%m-%d %H:%M:%S')
    else:
        comp_dict['last_contact_time_utc'] = 'Unknown'
    comp_dict['site'] = computer.site.name
    return comp_dict

# Create your views here.
@login_required
def home(request):
    return render(request, "index.html")


@login_required
def devices(request):
    devices = [_format_device(computer) for computer in Computer.objects.all()]
    context = {
        'items': devices,
        'columns': (
            ('name', 'Name'), 
            ('asset_tag', 'Asset Tag'),
            ('mac_address', 'MAC Address'),
            ('jamf_version', 'JAMF Version'),
            ('last_contact_time_utc', 'Last Check-in'),
            ('site', 'Site')
        ),
        'page_title': 'Computers',
        'menu_active': 'devices',
        'link_column': ('name', 'singledevice'),
    }
    return render(request, "list.html", context)


@login_required
def applications(request):
    applications = list()
    for app in ComputerApplication.objects.all():
        application = app.__dict__
        application['install_count'] = app.computers.count()
        applications.append(application)
    # applications = [app.__dict__ for app in ComputerApplication.objects.all()]
    context = {
        'items': applications,
        'columns': (
            ('name', 'Name'), 
            ('version', 'Version'),
            ('path', 'Path'),
            ('install_count', 'Install Count')
        ),
        'link_column': ('install_count', 'application-installed'),
        'page_title': 'Applications',
        # 'menu_active': 'devices'
    }
    return render(request, "list.html", context)

@login_required
def application_installed_list(request, pk):
    application = get_object_or_404(ComputerApplication, pk=pk)
    computers = [_format_device(computer) for computer in application.computers.all()]
    page_title = 'Computers with {name} ({version})'.format(
        name=application.name, version=application.version
    )
    context = {
        'items': computers,
        'columns': (
            ('name', 'Name'), 
            ('asset_tag', 'Asset Tag'),
            ('mac_address', 'MAC Address'),
            ('jamf_version', 'JAMF Version'),
            ('last_contact_time_utc', 'Last Check-in'),
            ('site', 'Site')
        ),
        'page_title': page_title,
        'link_column': ('name', 'singledevice'),
        'menu_active': 'devices'
    }
    return render(request, "list.html", context)


@login_required  
def singledevice(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer_dict = _format_device(computer)
    installed_applications = [application.__dict__ for application in computer.applications.all()]
    context = {
        'device': computer_dict,
        'items': installed_applications,
        'columns': (
            ('name', 'Name'), 
            ('version', 'Version'),
            ('path', 'Path'),
        ),
        'link_column': ('application-installed'),
        'page_title': 'Applications',

    }
    return render(request, "singledevice.html", context)    
