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
                'display_position': player.display_position,  # ¡AÑADE ESTA LÍNEA!
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
    
    # Get next match (first future match where scores aren't set) - SOLO SENIOR A
    next_match = Match.objects.filter(
        date__gte=now,
        home_score__isnull=True,
        away_score__isnull=True,
        team_category='senior_a'  # Filtra solo Senior A
    ).order_by('date').first()
    
    # Get last three completed matches - SOLO SENIOR A
    last_matches = Match.objects.filter(
        date__lte=now,
        home_score__isnull=False,
        away_score__isnull=False,
        team_category='senior_a'  # Filtra solo Senior A
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

from django.db import models  # Añade esta importación


# views.py
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET
from django.views.decorators.cache import never_cache
from .models import Match

import logging
logger = logging.getLogger(__name__)

@never_cache
@require_GET
def get_next_match(request):
    try:
        team = request.GET.get('team')
        
        if team in ['senior_a', 'senior_b']:
            now = timezone.now()
            
            # USAR EL MISMO FILTRO QUE LA VISTA HOME
            next_match = Match.objects.filter(
                date__gte=now,
                home_score__isnull=True,  # ← Añadir este filtro
                away_score__isnull=True   # ← Añadir este filtro
            ).filter(
                team_category=team  # Filtrar por categoría
            ).order_by('date').first()
            
            if next_match:
                # Determinar si Olympia es home o away
                is_olympia_home = "OLYMPIA" in next_match.home_team.upper()
                is_olympia_away = "OLYMPIA" in next_match.away_team.upper()
                
                if is_olympia_home:
                    opponent_team = next_match.away_team
                    opponent_logo = next_match.away_team_logo
                elif is_olympia_away:
                    opponent_team = next_match.home_team
                    opponent_logo = next_match.home_team_logo
                else:
                    opponent_team = next_match.away_team
                    opponent_logo = next_match.away_team_logo
                
                opponent_logo_url = ""
                if opponent_logo:
                    try:
                        opponent_logo_url = opponent_logo.url
                    except:
                        pass
                
                return JsonResponse({
                    'date': next_match.date.strftime('%a, %d %b'),
                    'time': next_match.date.strftime('%H:%M H'),
                    'location': next_match.location_name or 'Por determinar',
                    'opponent': opponent_team,
                    'opponent_logo': opponent_logo_url,
                    'fixture': getattr(next_match, 'fixture', '') or '',
                    'is_home': is_olympia_home
                })
        
        return JsonResponse({})
        
    except Exception as e:
        print(f"DEBUG: Error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

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








# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
import json

def registration_form(request):
    return render(request, 'registration_form.html')

# views.py
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Inscription

def get_csrf_token(request):
    """Helper function to get CSRF token"""
    from django.middleware.csrf import get_token
    return get_token(request)

@csrf_exempt
def create_inscription(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid JSON format'
                }, status=400)
            
            # Validate required fields - UPDATED WITH ALL NECESSARY FIELDS
            required_fields = [
                'full_name', 'birthdate', 'category', 'birth_municipality', 
                'empadronamiento', 'landline', 'address', 'city', 'zip_code',
                'mother_name', 'mother_dni', 'mother_email', 'mother_phone', 'mother_birthplace',
                'club_rules', 'privacy_policy', 'health_data'
            ]
            missing_fields = [field for field in required_fields if field not in data or not data[field]]
            
            if missing_fields:
                return JsonResponse({
                    'status': 'error',
                    'message': f'Missing required fields: {", ".join(missing_fields)}'
                }, status=400)
            
            # Generate inscription number without saving to DB
            import uuid
            inscription_number = str(uuid.uuid4())[:8].upper()
            
            # Send emails
            send_inscription_emails(data, inscription_number)
            
            return JsonResponse({
                'status': 'success',
                'inscription_number': inscription_number,
                'message': 'Inscripción recibida correctamente'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Error processing inscription: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Only POST requests are allowed'
    }, status=405)

def send_inscription_emails(data, inscription_number):
    """Send confirmation emails - UPDATED WITH ALL FIELDS"""
    try:
        # Email to customer
        customer_subject = f'Confirmación de inscripción #{inscription_number} - Club Olympia'
        customer_message = f'''
Gracias por tu inscripción en Club Olympia!

Detalles de tu inscripción:
Número de inscripción: {inscription_number}
Nombre: {data['full_name']}
Categoría: {data['category']}
Fecha de nacimiento: {data['birthdate']}

Hemos recibido tu solicitud y nos pondremos en contacto contigo pronto para completar el proceso.

Para cualquier consulta, puedes contactarnos en inscripciones@olympia.com

¡Te damos la bienvenida a Olympia!
'''
        
        # Use appropriate email (player email if available, otherwise parent email)
        recipient_email = data.get('email') or data.get('mother_email')  # Player email or mother's email
        
        if recipient_email:
            send_mail(
                customer_subject,
                customer_message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
        
        # Email to club - UPDATED WITH ALL FIELDS
        club_subject = f'Nueva inscripción #{inscription_number} - {data["full_name"]}'
        club_message = f'''
Nueva inscripción recibida en el sistema:

INFORMACIÓN PERSONAL:
Nombre: {data['full_name']}
Fecha de nacimiento: {data['birthdate']}
Categoría: {data['category']}
Municipio de nacimiento: {data['birth_municipality']}
Empadronamiento: {data['empadronamiento']}
DNI Jugadora: {data.get('player_dni', 'No proporcionado')}
Email Jugadora: {data.get('email', 'No proporcionado')}
Teléfono Jugadora: {data.get('phone', 'No proporcionado')}
Teléfono Fijo: {data['landline']}

DOMICILIO:
Dirección: {data['address']}
Población: {data['city']}
Código Postal: {data['zip_code']}

EXPERIENCIA PREVIA:
¿Ha jugado antes?: {data.get('played_before', 'No especificado')}
Equipos anteriores y posición: {data.get('previous_teams', 'No especificado')}

DATOS DE LA MADRE/TUTOR:
Nombre: {data['mother_name']}
DNI: {data['mother_dni']}
Email: {data['mother_email']}
Teléfono: {data['mother_phone']}
Lugar de nacimiento: {data['mother_birthplace']}

DATOS DEL PADRE (OPCIONAL):
Nombre: {data.get('father_name', 'No proporcionado')}
DNI: {data.get('father_dni', 'No proporcionado')}
Email: {data.get('father_email', 'No proporcionado')}
Teléfono: {data.get('father_phone', 'No proporcionado')}
Lugar de nacimiento: {data.get('father_birthplace', 'No proporcionado')}

CONSENTIMIENTOS:
Normas del club: {'Aceptado' if data.get('club_rules') else 'No aceptado'}
Política de privacidad: {'Aceptado' if data.get('privacy_policy') else 'No aceptado'}
Datos de salud: {'Aceptado' if data.get('health_data') else 'No aceptado'}
Imagen redes sociales: {'Aceptado' if data.get('social_media_image') else 'No aceptado'}
Imagen internet: {'Aceptado' if data.get('internet_image') else 'No aceptado'}
Publicidad: {'Aceptado' if data.get('marketing') else 'No aceptado'}

DATOS BANCARIOS:
Titular de la cuenta: {data['account_holder']}
DNI Titular: {data['account_holder_dni']}
Dirección: {data['account_holder_address']}
C.P.: {data['account_holder_zip']} Población: {data['account_holder_city']}
Provincia: {data['account_holder_province']}
SWIFT Code: {data.get('swift_code', 'No proporcionado')}
IBAN: {data['iban']}
Tipo de Pago: {data['payment_type']}
Fecha de firma: {data['signature_date']}

AUTORIZACIÓN MENOR:
Fecha autorización: {data['authorization_date']}
Firma madre/tutora: {data['mother_signature_name']} (DNI: {data['mother_signature_dni']})
Firma padre/tutor: {data.get('father_signature_name', 'No proporcionada')}
Declaración responsable: {data.get('single_parent_reason', 'No aplica')}
Otras circunstancias: {data['other_reason']} if data.get('other_reason') else ''


# Añadir esta sección en el email al club
PROTECCIÓN DE DATOS:
Firma: {data['data_protection_signature_name']} (DNI: {data['data_protection_signature_dni']})
Consentimiento protección datos: {'Sí' if data.get('data_protection_consent') else 'No'}

CARTA COMPROMISO:
Fecha compromiso: {data['commitment_date']}
Firma jugadora: {data['player_signature']}
Firma tutor: {data['parent_signature']}
Compromisos aceptados: 
- Comportamiento: {'Sí' if data.get('commitment_behavior') else 'No'}
- Deportividad: {'Sí' if data.get('commitment_sportsmanship') else 'No'}
- Redes sociales: {'Sí' if data.get('commitment_social_media') else 'No'}
- Entrenador: {'Sí' if data.get('commitment_coach') else 'No'}
- Puntualidad: {'Sí' if data.get('commitment_punctuality') else 'No'}
- Comunicación: {'Sí' if data.get('commitment_communication') else 'No'}

DATOS DE LA INSCRIPCIÓN:
Número: {inscription_number}
Temporada: {data.get('season', '2025/2026')}
Cuota: {data.get('registration_fee', '130')}€
'''
        
       # Send to club email - FIXED EMAIL CONFIGURATION
        club_email = getattr(settings, 'CLUB_EMAIL', 'moezehero@gmail.com')
        print(f"DEBUG: Intentando enviar email al club: {club_email}")
        
        try:
            send_mail(
                club_subject,
                club_message,
                settings.DEFAULT_FROM_EMAIL,
                [club_email],
                fail_silently=False,
            )
            print("DEBUG: Email enviado al club correctamente")
        except Exception as e:
            print(f"ERROR: No se pudo enviar email al club: {str(e)}")
            # Intentar enviar a un email alternativo
            try:
                send_mail(
                    "ERROR - Inscripción no notificada",
                    f"No se pudo enviar la notificación de inscripción #{inscription_number} al club. Error: {str(e)}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],  # Enviar a sí mismo para notificar el error
                    fail_silently=False,
                )
            except:
                print("ERROR: No se pudo enviar email de error")
        
    except Exception as e:
        print(f"Error sending email: {e}")
        # Don't fail the entire request if email fails



# views.py
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

# views.py
@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            print("Solicitud recibida para PaymentIntent")
            print("Clave API:", settings.STRIPE_SECRET_KEY[:20] + "...")  # Muestra solo parte de la clave
            # Asegúrate de que la clave secreta esté configurada
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            # Verifica que estás usando una clave de test válida
            if not stripe.api_key.startswith('sk_test_'):
                return JsonResponse({'error': 'Clave secreta inválida'}, status=400)
            
            # Crea el Payment Intent con parámetros correctos
            intent = stripe.PaymentIntent.create(
                amount=13000,  # 130€ en céntimos
                currency='eur',
                automatic_payment_methods={
                    'enabled': True,
                },
                metadata={
                    'inscription_id': 'temp_id'
                }
            )
            
            # Verifica que el client_secret se devuelve correctamente
            return JsonResponse({
                'clientSecret': intent.client_secret,
                'paymentIntentId': intent.id
            })
            
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Error interno'}, status=500)
        


def payment_success(request):
    """Vista para cuando el pago es exitoso"""
    payment_intent_id = request.GET.get('payment_intent')
    payment_status = request.GET.get('redirect_status')
    
    # Aquí puedes guardar en la base de datos que el pago fue exitoso
    # y marcar la inscripción como pagada
    
    context = {
        'payment_intent_id': payment_intent_id,
        'status': payment_status
    }
    

def payment_cancel(request):
    """Vista para cuando el pago es cancelado"""




# views.py - Cambia las URLs de éxito y cancelación
@csrf_exempt
@require_POST
def create_checkout_session(request):
    try:
        data = json.loads(request.body)
        
        # Create line items for Stripe
        line_items = []
        for item in data.get('items', []):
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': item['name'],
                        'metadata': {
                            'size': item.get('size', ''),
                            'color': item.get('color', ''),
                            'customization': item.get('customization', '')
                        }
                    },
                    'unit_amount': item['price'],
                },
                'quantity': item['quantity'],
            })

        # Obtener la URL base
        base_url = settings.FRONTEND_URL if hasattr(settings, 'FRONTEND_URL') else 'http://127.0.0.1:8000'
        
        # Create checkout session - Redirigir a la tienda con parámetros
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f"{base_url}/tienda?payment=success&session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{base_url}/tienda?payment=cancelled",
            customer_email=data.get('customer_email'),
            metadata={
                'customer_name': data.get('customer_name'),
                'customer_phone': data.get('customer_phone'),
                'customer_category': data.get('customer_category', ''),
                'order_type': 'merchandising'
            }
        )

        return JsonResponse({'sessionId': checkout_session.id})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    
# views.py
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        try:
            # Find the order in your database
            # order = Order.objects.get(stripe_session_id=session.id)
            
            # Update order status to completed
            # order.status = 'completed'
            # order.payment_intent_id = session.payment_intent
            # order.save()
            
            # Send confirmation email
            # send_order_confirmation_email(order)
            
            print(f"Payment successful for session {session.id}")
            
        except Exception as e:
            print(f"Error processing webhook: {str(e)}")

    return HttpResponse(status=200)

# views.py
def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        try:
            # Retrieve session from Stripe
            session = stripe.checkout.Session.retrieve(session_id)
            
            # Get order from database
            # order = Order.objects.get(stripe_session_id=session_id)
            
            context = {
                'session': session,
                # 'order': order
            }
            
            return render(request, 'base/payment_success.html', context)
            
        except Exception as e:
            # Handle error
            pass
    
    return render(request, 'base/payment_success.html')

from django.shortcuts import render

def contactos(request):
    context = {
        'title': 'Contactos - CFF Olympia',
    }
    return render(request, 'base/contactos.html', context)