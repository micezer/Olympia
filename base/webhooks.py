import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

    # Manejar eventos de pago
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        handle_payment_succeeded(payment_intent)
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        handle_payment_failed(payment_intent)

    return HttpResponse(status=200)

def handle_payment_succeeded(payment_intent):
    # Aquí procesas el pago exitoso
    # Actualizar base de datos, enviar email, etc.
    print(f"Pago exitoso: {payment_intent['id']}")

def handle_payment_failed(payment_intent):
    # Aquí manejas el pago fallido
    print(f"Pago fallido: {payment_intent['id']}")



