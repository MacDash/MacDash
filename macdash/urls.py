"""macdash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# Add this import
from django.contrib.auth.views import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()
admin.site.login = login_required(admin.site.login)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('dash.urls')),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'), 
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'), 
]
