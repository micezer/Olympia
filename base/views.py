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

from django.http import FileResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage
from .utils.pdf import generar_pdf_inscripcion
from django.http import JsonResponse

from datetime import datetime
logger = logging.getLogger(__name__)


import logging
logger = logging.getLogger(__name__)

# views.py
from django.shortcuts import render
def offline(request):
    return render(request, 'offline.html')

def inscripcion_view(request):
    return render(request, 'base/inscripcion.html')

def cantera_view(request):
    return render(request, 'base/cantera.html')

def download_view(request):
    return render(request, 'base/download.html')
def about_view(request):
    return render(request, 'base/about.html')


def serviceworker(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'serviceworker.js')
    return FileResponse(open(path, 'rb'), content_type='application/javascript')

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.conf import settings
import json

@never_cache
def manifest(request):
    manifest_data = {
        "name": "CFF Olympia",
        "short_name": "CFF Olympia",
        "start_url": "/",
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
    return render(request, 'base/home.html')




logger = logging.getLogger(__name__)

def test_form(request):
    # Renderiza el formulario
    return render(request, 'base/test_form.html')

logger = logging.getLogger(__name__)

def formulario_inscripcion(request):
    if request.method == 'GET':
        return render(request, 'base/test_form.html')
    
    if request.method == 'POST':
        try:
            # Recoger datos del formulario
            datos = {
                'nombre_completo': request.POST.get('nombre_completo'),
                'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
                'dni': request.POST.get('dni'),
                'posicion': request.POST.get('posicion'),
                'club_anterior': request.POST.get('club_anterior', 'Ninguno'),
                'email': request.POST.get('email'),
                'contacto_emergencia': request.POST.get('contacto_emergencia')
            }

            # Generar PDF
            pdf = generar_pdf_inscripcion(datos)

            # Configurar y enviar email
            email = EmailMessage(
                subject=f"Nueva Inscripción: {datos['nombre_completo']}",
                body=f"""
                Nueva jugadora registrada:
                Nombre: {datos['nombre_completo']}
                Edad: {datos['fecha_nacimiento']}
                Posición: {datos['posicion']}
                
                PDF adjunto con detalles completos.
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['obiezeh999@gmail.com'],
                reply_to=[datos['email']],
            )
            
            email.attach(
                f"inscripcion_{datos['dni']}.pdf",
                pdf.getvalue(),
                "application/pdf"
            )
            
            email.send(fail_silently=False)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Inscripción enviada correctamente'
            })
            
        except Exception as e:
            logger.error(f"Error en inscripción: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': 'Error al procesar la inscripción'
            }, status=500)