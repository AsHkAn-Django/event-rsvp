from celery import shared_task
from django.core.mail import EmailMessage
from io import BytesIO
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from order.models import Order
import weasyprint



@shared_task
def send_successful_payment_email(order_id):
    """
    Task to send an e-mail notification, QR code and
    the Ticket to user when an order is successfully paid.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Event RSVP - Ticket no. {order_id}'
    message = 'Your Ticket with QR code has been attached to this email.'
    email = EmailMessage(subject, message, from_email=None, to=[order.email])

    html = render_to_string('order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(finders.find('css/pdf.css'))]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f'order_{order_id}.pdf', out.getvalue(), 'application/pdf')
    email.send()