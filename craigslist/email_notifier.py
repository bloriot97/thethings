from django.core.mail import send_mail
from .models import Announce

def announce_creation(announce):
    subject = 'Announce #{0} created'.format(announce.pk)
    body = 'Dear {0}, Your announce {1} has been created'.format(announce.author_name, announce.title)
    send_mail(
        subject,
        body,
        'no-reply@thethings.com',
        [announce.author_email],
        fail_silently=False,
    )
