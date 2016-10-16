from django.shortcuts import render, get_object_or_404
# from django.conf import settings
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext

from jss.models import Computer, ComputerApplication

# Create your views here.
@login_required
def home(request):
    return render(request, "index.html")


@login_required
def devices(request):
    context = {
        'items': Computer.objects.all(),
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
    context = {
        'items': ComputerApplication.objects.all(),
        'columns': (
            ('name', 'Name'),
            ('version', 'Version'),
            ('path', 'Path'),
        ),
        'link_column': ('name', 'application-installed'),
        'page_title': 'Applications',
        'menu_active': 'applications',
    }
    return render(request, "list.html", context)

@login_required
def application_installed_list(request, pk):
    application = get_object_or_404(ComputerApplication, pk=pk)
    page_title = 'Computers with {name} ({version})'.format(
        name=application.name, version=application.version
    )
    context = {
        'items': application.computers.all(),
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
    context = {
        'device': computer,
        'items': computer.applications.all(),
        'columns': (
            ('name', 'Name'),
            ('version', 'Version'),
            ('path', 'Path'),
        ),
        'link_column': ('name', 'application-installed'),
        'page_title': 'Applications',

    }
    return render(request, "singledevice.html", context)
