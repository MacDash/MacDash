# dash/urls.py
from django.conf.urls import url

from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^singledevice/(?P<pk>[0-9]+)$', views.singledevice, name='singledevice'),
    url(r'^applications/$', views.applications, name='applications'),
    url(r'^applications/(?P<pk>[0-9]+)/installed/', 
        views.application_installed_list, 
        name='application-installed')
]

