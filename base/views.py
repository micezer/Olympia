# Django core
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
# Autenticación
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache





import logging
logger = logging.getLogger(__name__)

# views.py
from django.shortcuts import render
def offline(request):
    return render(request, 'offline.html')

def inscripciones_view(request):
    return render(request, 'base/inscripciones.html')

def cantera_view(request):
    return render(request, 'base/cantera.html')

def download_view(request):
    return render(request, 'base/download.html')
def about_view(request):
    return render(request, 'base/about.html')

def service_worker(request):
    response = HttpResponse(
        open(os.path.join(settings.STATIC_ROOT, 'js/sw.js')).read(), 
        content_type='application/javascript'
    )
    response['Service-Worker-Allowed'] = '/'
    return response

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.conf import settings
import json

@never_cache
def manifest(request):
    manifest_data = {
        "name": "CFF Olympia",
        "short_name": "CFF Olympia",
        "start_url": "/home/?v=2",
        "display": "standalone",
        "background_color": "#000000",
        "theme_color": "#FFD700",
        "icons": [
            {
                "src": f"{settings.STATIC_URL}images/icons/olympia-icon-192x192.png?v=2",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": f"{settings.STATIC_URL}images/icons/olympia-icon-512x512.png?v=2",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    return HttpResponse(json.dumps(manifest_data), content_type='application/json')

def home(request):
    if request.user.is_authenticated:
        user_services = request.user.userprofile.services.all()
    else:
        user_services = None
    return render(request, 'base/home.html', {'user_services': user_services})





