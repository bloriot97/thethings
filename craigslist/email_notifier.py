from django.core.mail import send_mail
from .models import Announce, Mail

def announce_creation(announce, request):
    subject = 'Announce #{0} created'.format(announce.pk)
    # there is no nice way to get the website url except to get it from the URL.
    # You could also define a Site object corresponding to your website.
    url = request.get_host() + announce.getEditUri()
    body = 'Dear {0}, Your announce {1} has been created <br> To edit it use this link : {2}'.format(announce.author_name, announce.title, url)
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
