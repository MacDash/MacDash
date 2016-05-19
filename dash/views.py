from django.shortcuts import render
# from django.shortcuts import render, redirect, get_object_or_404
# from django.conf import settings
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def home(request):
    return render(request, "index.html")