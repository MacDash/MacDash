from django.shortcuts import render
# from django.shortcuts import render, redirect, get_object_or_404
# from django.conf import settings
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from jss.models import Computer

# Create your views here.
@login_required
def home(request):
    return render(request, "index.html")

@login_required
def devices(request):
    devices = list()
    computers = Computer.objects.all()
    for computer in Computer.objects.all():
        comp_dict = computer.__dict__
        if computer.last_contact_time_utc:
            comp_dict['last_contact_time_utc'] = computer.last_contact_time_utc.strftime('%Y-%m-%d %H:%M:%S')
        else:
            comp_dict['last_contact_time_utc'] = 'Unknown'
        devices.append(comp_dict)
    return render(request, "list.html", {'items': devices, 'list_title': 'Computers', 'menu_active': 'devices'})