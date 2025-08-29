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
# views.py
from django.utils import timezone
from django.shortcuts import render
from .models import Match

import logging
logger = logging.getLogger(__name__)

# views.py
from django.shortcuts import render
def offline(request):
    return render(request, 'offline.html')

def inscripcion_view(request):
    return render(request, 'base/inscripcion.html')

# views.py
from django.http import JsonResponse
from .models import Player

def get_players_by_team(request):
    team = request.GET.get('team')
    if team:
        players = Player.objects.filter(team=team).order_by('number')
        players_data = []
        for player in players:
            players_data.append({
                'id': player.id,
                'name': player.name,
                'full_name': player.full_name,
                'number': player.number,
                'position': player.position,
                'team': player.team,
                'birth_date': player.birth_date.strftime('%Y-%m-%d') if player.birth_date else None,
                'nationality': player.nationality,
                'image': player.image.url if player.image else None,
                'is_staff': player.is_staff,
                'role': player.role,
            })
        return JsonResponse(players_data, safe=False)
    return JsonResponse([], safe=False)

def cantera_view(request):
    # Get all players grouped by team
    senior_a_players = Player.objects.filter(team='senior_a')
    senior_b_players = Player.objects.filter(team='senior_b')
    
    # Get staff members (is_staff=True)
    staff_members = Player.objects.filter(is_staff=True)
    
    context = {
        'senior_a_players': senior_a_players,
        'senior_b_players': senior_b_players,
        'staff_members': staff_members,
    }
    return render(request, 'base/cantera.html', context)

def tienda_view(request):
    return render(request, 'base/tienda.html')

def ticket_purchase(request):
    return render(request, 'base/ticket_purchase.html')


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


# Get an instance of a logger
logger = logging.getLogger(__name__)

# views.py
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Match

# views.py
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Match

@never_cache
def home(request):
    # Get current time in the correct time zone
    now = timezone.now()
    
    # Get next match (first future match where scores aren't set)
    next_match = Match.objects.filter(
        date__gte=now,
        home_score__isnull=True,
        away_score__isnull=True
    ).order_by('date').first()
    
    # Get last three completed matches
    last_matches = Match.objects.filter(
        date__lte=now,
        home_score__isnull=False,
        away_score__isnull=False
    ).order_by('-date')[:3]
    
    context = {
        'next_match': next_match,
        'last_matches': last_matches,
        'current_time': now,
    }
    
    response = render(request, 'base/home.html', context)
    # Add headers to prevent caching
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = 'Fri, 01 Jan 1990 00:00:00 GMT'
    return response




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
        

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Ticket
import json
from datetime import datetime

@csrf_exempt
def purchase_ticket(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Create ticket
            ticket = Ticket.objects.create(
                dni=data['dni'],
                full_name=data['fullName'],
                email=data['email'],
                match=data['match'],
                section=data['section'],
                seat=data['seat'],
                qr_code=data['qrCode'],
                ticket_type='single' if data['ticketType'] == 'Entrada Individual' else 'season',
                price=float(data['price'].replace('€', ''))
            )
            
            # Send confirmation email
            send_mail(
                f"Confirmación de entrada - {ticket.match}",
                f"""Hola {ticket.full_name},
                
Gracias por comprar tu entrada para {ticket.match}.
                
Detalles:
- Tipo: {ticket.get_ticket_type_display()}
- Tribuna: {ticket.section}
- Asiento: {ticket.seat}
- Precio: €{ticket.price}
- Código QR: {ticket.qr_code}
                
Presenta este código QR en la entrada del estadio.""",
                'no-reply@yourclub.com',
                [ticket.email],
                fail_silently=False,
            )
            
            return JsonResponse({'status': 'success', 'ticket_id': ticket.id})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
def get_tickets(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dni = data.get('dni', '')
            
            tickets = Ticket.objects.filter(dni=dni).values(
                'id', 'dni', 'full_name', 'match', 'section', 
                'seat', 'purchase_date', 'is_used', 'qr_code',
                'ticket_type', 'price'
            )
            
            # Format dates
            tickets_list = list(tickets)
            for ticket in tickets_list:
                ticket['purchase_date'] = ticket['purchase_date'].strftime('%Y-%m-%d %H:%M')
                
            return JsonResponse({'status': 'success', 'tickets': tickets_list})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
import json
from .models import PlayerRegistration

def registration_form(request):
    return render(request, 'registration_form.html')

# views.py
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import PlayerRegistration
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class CheckRegistrationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            dni = data.get('dni', '').strip()
            
            if not dni:
                return JsonResponse({'error': 'DNI is required'}, status=400)
            
            try:
                player = PlayerRegistration.objects.get(dni=dni)
                return JsonResponse({
                    'exists': True,
                    'dni': player.dni,
                    'name': player.name,
                    'surname': player.surname,
                    'birthday': player.birthday.isoformat() if player.birthday else None,
                    'position': player.position,
                    'team': player.team,
                    'blood_type': player.blood_type,
                    'allergies': player.allergies,
                    'emergency_contact_name': player.emergency_contact_name,
                    'emergency_contact_phone': player.emergency_contact_phone,
                    'emergency_contact_relationship': player.emergency_contact_relationship,
                    'equipment_size': player.equipment_size,
                    'previous_experience': player.previous_experience,
                    'registration_complete': player.registration_complete
                })
            except PlayerRegistration.DoesNotExist:
                return JsonResponse({'exists': False})
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class SaveRegistrationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            dni = data.get('dni', '').strip()
            current_step = data.get('current_step', 1)
            
            if not dni:
                return JsonResponse({'error': 'DNI is required'}, status=400)
            
            # Validate DNI format (adjust based on your country's requirements)
            if not re.match(r'^[0-9]{7,10}$', dni):
                return JsonResponse({'error': 'Invalid DNI format'}, status=400)
            
            # Get or create player registration
            player, created = PlayerRegistration.objects.get_or_create(dni=dni)
            
            # Update fields based on the current step
            if current_step >= 1:
                # Step 1 is just DNI, which we already have
                pass
                
            if current_step >= 2:
                player.name = data.get('nombre', '')
                player.surname = data.get('apellido', '')
                birthday = data.get('fecha_nacimiento')
                if birthday:
                    player.birthday = birthday
                
            if current_step >= 3:
                player.position = data.get('posicion', '')
                player.team = data.get('equipo', '')
                
            if current_step >= 4:
                player.blood_type = data.get('tipo_sangre', '')
                player.allergies = data.get('alergias', '')
                player.emergency_contact_name = data.get('contacto_emergencia_nombre', '')
                player.emergency_contact_phone = data.get('contacto_emergencia_telefono', '')
                player.emergency_contact_relationship = data.get('contacto_emergencia_parentesco', '')
                
            if current_step >= 5:
                player.equipment_size = data.get('talla_equipacion', '')
                player.previous_experience = data.get('experiencia_previa', '')
                player.registration_complete = True
                
            player.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'Registration saved successfully',
                'current_step': current_step,
                'registration_complete': player.registration_complete
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_POST, name='dispatch')
class RecoverDataView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            dni = data.get('dni', '').strip()
            
            if not dni:
                return JsonResponse({'error': 'DNI is required'}, status=400)
            
            try:
                player = PlayerRegistration.objects.get(dni=dni)
                return JsonResponse({
                    'exists': True,
                    'dni': player.dni,
                    'name': player.name,
                    'surname': player.surname,
                    'birthday': player.birthday.isoformat() if player.birthday else None,
                    'position': player.position,
                    'team': player.team,
                    'blood_type': player.blood_type,
                    'allergies': player.allergies,
                    'emergency_contact_name': player.emergency_contact_name,
                    'emergency_contact_phone': player.emergency_contact_phone,
                    'emergency_contact_relationship': player.emergency_contact_relationship,
                    'equipment_size': player.equipment_size,
                    'previous_experience': player.previous_experience,
                    'registration_complete': player.registration_complete
                })
            except PlayerRegistration.DoesNotExist:
                return JsonResponse({'exists': False})
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)