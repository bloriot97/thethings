from django.core.mail import send_mail
from .models import Announce, Mail

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


def new_mail(mail):
    subject = 'New mail from {0} for the announce {1}'.format(mail.author_name, mail.announce.title)
    body = mail.body
    send_mail(
        subject,
        body,
        'no-reply@thethings.com',
        [mail.announce.author_email],
        fail_silently=False,
    )
