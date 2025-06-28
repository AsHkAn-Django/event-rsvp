from django.core.mail import EmailMessage
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from django.conf import settings
from django.core.files.base import ContentFile

from celery import shared_task
from order.models import Order

import weasyprint
import os
import qrcode
from io import BytesIO



DOMAIN = 'http://127.0.0.1:8000/'


@shared_task
def send_successful_payment_email(order_id):
    order = Order.objects.get(id=order_id)

    subject = f'Event RSVP - Ticket no. {order_id}'
    message = 'Your Ticket has been attached to this email.'
    email = EmailMessage(subject, message, from_email=None, to=[order.email])

    # Create PDF
    html = render_to_string('order/pdf.html', {'order': order})
    pdf_output_dir = os.path.join(settings.MEDIA_ROOT, 'tickets')
    os.makedirs(pdf_output_dir, exist_ok=True)
    pdf_filename = f'ticket_order_{order.id}.pdf'
    pdf_path = os.path.join(pdf_output_dir, pdf_filename)
    stylesheets = [weasyprint.CSS(finders.find('css/pdf.css'))]
    pdf_bytes = weasyprint.HTML(string=html).write_pdf(stylesheets=stylesheets)

    # Save PDF file to model
    order.ticket_file.save(pdf_filename, ContentFile(pdf_bytes))

    # Create QR code
    pdf_url = DOMAIN + settings.MEDIA_URL + 'tickets/' + pdf_filename
    qr = qrcode.make(pdf_url)
    qr_io = BytesIO()
    qr.save(qr_io)
    qr_io.seek(0)
    order.qr_file.save(f'qr_{order.id}.png', ContentFile(qr_io.read()))

    order.save()

    email.attach(pdf_filename, pdf_bytes, 'application/pdf')
    email.send()
