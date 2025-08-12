require('dotenv').config();
const express = require('express');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const bodyParser = require('body-parser');
const fetch = require('node-fetch');
const app = express();

// Middleware
app.use(express.static('public')); // Serve static files
app.use(bodyParser.json());

// Stripe Checkout endpoint
app.post('/create-checkout-session', async (req, res) => {
  try {
    const { items, customerEmail, customerName, orderData } = req.body;
    
    // Calculate total amount
    const lineItems = items.map(item => ({
      price_data: {
        currency: 'eur',
        product_data: {
          name: item.name,
          description: item.size ? `Talla: ${item.size}` : '',
        },
        unit_amount: Math.round(item.price * 100),
      },
      quantity: item.quantity || 1,
    }));

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: lineItems,
      mode: 'payment',
      success_url: `${process.env.YOUR_DOMAIN}/tienda?session_id={CHECKOUT_SESSION_ID}&payment_status=success`,
      cancel_url: `${process.env.YOUR_DOMAIN}/tienda?canceled=true`,
      customer_email: customerEmail,
      metadata: {
        customer_name: customerName,
        order_data: JSON.stringify(orderData)
      }
    });

    res.json({ id: session.id });
  } catch (err) {
    console.error('Error creating checkout session:', err);
    res.status(500).json({ error: err.message });
  }
});

// Stripe webhook for payment confirmation
app.post('/stripe-webhook', bodyParser.raw({type: 'application/json'}), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    console.error('Webhook error:', err);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle successful payment
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const orderData = JSON.parse(session.metadata.order_data);
    orderData.payment_id = session.payment_intent;
    orderData.payment_status = 'PAID';
    
    await sendConfirmationEmail(orderData);
  }

  res.json({ received: true });
});

async function sendConfirmationEmail(orderData) {
  const formSubmitEndpoint = "https://formsubmit.co/ajax/your@email.com";
  
  try {
    await fetch(formSubmitEndpoint, {
      method: "POST",
      headers: { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        name: "Confirmación de Pago Tienda Olympia",
        message: formatConfirmationEmail(orderData),
        _subject: `Confirmación de pago - Pedido de ${orderData.name}`,
        _template: "table",
        _captcha: "false"
      })
    });
  } catch (error) {
    console.error("Error sending confirmation email:", error);
  }
}

function formatConfirmationEmail(orderData) {
  return `
    <h2>¡Pago confirmado!</h2>
    <p>Gracias por tu compra en la Tienda Olympia. Aquí están los detalles de tu pedido:</p>
    
    <p><strong>Número de pedido:</strong> ${orderData.payment_id || 'N/A'}</p>
    <p><strong>Nombre:</strong> ${orderData.name}</p>
    <p><strong>Email:</strong> ${orderData.email}</p>
    <p><strong>Teléfono:</strong> ${orderData.phone}</p>
    <p><strong>Total pagado:</strong> ${orderData.total}</p>
    <p><strong>Fecha:</strong> ${orderData.date}</p>
    
    <h3>Productos:</h3>
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
      <thead>
        <tr>
          <th>Producto</th>
          <th>Talla</th>
          <th>Color</th>
          <th>Personalización</th>
          <th>Precio</th>
          <th>Cantidad</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        ${orderData.items.map(item => `
          <tr>
            <td>${item.name}</td>
            <td>${item.size}</td>
            <td>${item.color}</td>
            <td>${item.customization}</td>
            <td>${item.price}</td>
            <td>${item.quantity}</td>
            <td>${item.total}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>
    
    <p>Nos pondremos en contacto contigo para coordinar la entrega.</p>
    <p>¡Gracias por apoyar al Club Olympia!</p>
  `;
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));