import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(items, customer_email, customer_name, order_data):
    try:
        line_items = [{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': item['name'],
                    'description': f"Size: {item.get('size', 'N/A')} | Color: {item.get('color', 'N/A')}"
                },
                'unit_amount': int(item['price'] * 100),
            },
            'quantity': item.get('quantity', 1),
        } for item in items]

        return stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f"{settings.YOUR_DOMAIN}/checkout/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{settings.YOUR_DOMAIN}/checkout/canceled",
            customer_email=customer_email,
            metadata={
                'customer_name': customer_name,
                'order_data': order_data
            }
        )
    except Exception as e:
        print(f"Stripe error: {str(e)}")
        raise