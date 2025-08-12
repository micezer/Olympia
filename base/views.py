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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

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

def tienda_view(request):
    return render(request, 'base/tienda.html')

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


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Order
import json

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            # Ensure we have JSON content
            if request.content_type != 'application/json':
                return JsonResponse({
                    'status': 'error',
                    'message': 'Content-Type must be application/json'
                }, status=400)
                
            data = json.loads(request.body)
            
            # Validate required fields
            required_fields = ['full_name', 'email', 'phone', 'total', 'items']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({
                        'status': 'error',
                        'message': f'Missing required field: {field}'
                    }, status=400)
            
            # Create the order
            order = Order(
                full_name=data['full_name'],
                email=data['email'],
                phone=data['phone'],
                category=data.get('category', ''),
                total=float(data['total']),
                items_json=json.dumps(data['items']),
                paid=True
            )
            order.save()
            
            # Send emails
            send_order_emails(order)
            
            return JsonResponse({
                'status': 'success',
                'order_number': order.order_number
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON format'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Only POST requests are allowed'
    }, status=405)

def send_order_emails(order):
    items = order.get_items()
    
    # Email to customer
    customer_subject = f'Confirmación de pedido #{order.order_number}'
    customer_message = f'''Gracias por tu pedido en Tienda Olympia!

Detalles del pedido:
Número de pedido: {order.order_number}
Fecha: {order.created_at.strftime("%d/%m/%Y %H:%M")}
Total: €{order.total:.2f}

Productos:
'''
    for item in items:
        customer_message += f"- {item['name']} (€{item['price']} x {item['quantity']})\n"
        if item.get('size'):
            customer_message += f"  Talla: {item['size']}\n"
        if item.get('color'):
            customer_message += f"  Color: {item['color']}\n"
        if item.get('customization'):
            customer_message += f"  Personalización: {item['customization']}\n"
    
    customer_message += '\nNos pondremos en contacto contigo pronto. ¡Gracias!'
    
    send_mail(
        customer_subject,
        customer_message,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        fail_silently=False,
    )
    
    # Email to owner
    owner_subject = f'Nuevo pedido #{order.order_number}'
    owner_message = f'''Nuevo pedido recibido!

Detalles del cliente:
Nombre: {order.full_name}
Email: {order.email}
Teléfono: {order.phone}
Categoría: {order.category or 'No especificada'}

Detalles del pedido:
Número de pedido: {order.order_number}
Fecha: {order.created_at.strftime("%d/%m/%Y %H:%M")}
Total: €{order.total:.2f}

Productos:
'''
    for item in items:
        owner_message += f"- {item['name']} (€{item['price']} x {item['quantity']})\n"
        if item.get('size'):
            owner_message += f"  Talla: {item['size']}\n"
        if item.get('color'):
            owner_message += f"  Color: {item['color']}\n"
        if item.get('customization'):
            owner_message += f"  Personalización: {item['customization']}\n"
    
    send_mail(
        owner_subject,
        owner_message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.OWNER_EMAIL],
        fail_silently=False,
    )


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