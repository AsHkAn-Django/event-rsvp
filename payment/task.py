from django.core.mail import EmailMessage
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from django.conf import settings
from django.core.files.base import ContentFile

from celery import shared_task
from order.models import Order

import weasyprint


@shared_task
def send_successful_payment_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Event RSVP - Ticket no. {order_id}'
    message = 'Your Ticket with QR code has been attached to this email.'
    email = EmailMessage(subject, message, from_email=None, to=[order.email])

    html = render_to_string('order/pdf.html', {'order': order})
    stylesheets = [weasyprint.CSS(finders.find('css/pdf.css'))]
    pdf_bytes = weasyprint.HTML(string=html).write_pdf(stylesheets=stylesheets)

    filename = f'ticket_order_{order.id}.pdf'
    order.ticket_file.save(filename, ContentFile(pdf_bytes)) 
    order.save()

    email.attach(filename, pdf_bytes, 'application/pdf')
    email.send()
