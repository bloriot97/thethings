from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

from . import email_notifier

import string
import random


from .models import Announce, Mail

# Create your views here.

def index(request):
    latest_annonce_list = Announce.objects.order_by('-edit_date')
    template = loader.get_template('craigslist/index.html')
    context = {
        'latest_annonce_list': latest_annonce_list,
    }
    return HttpResponse(template.render(context, request))

def announce_detail(request, announce_id):
    announce = get_object_or_404(Announce, pk=announce_id)
    return render(request, 'craigslist/detail.html', {'announce': announce})

def contact(request, announce_id):
    announce = get_object_or_404(Announce, pk=announce_id)
    return render(request, 'craigslist/contact.html', {'announce': announce})

def new(request):
    return render(request, 'craigslist/new.html')

def send_mail(request, announce_id):
    # Here I should check if the informations are valid, but as they are already verified on the client side we are going to concider for this project that they are well formed
    announce = get_object_or_404(Announce, pk=announce_id)
    try:
        name = request.POST['name']
        email = request.POST['email']
        body = request.POST['body']
        date = timezone.now()
    except (KeyError):
        return HttpResponse("error")
    else:
        mail = Mail(announce=announce, body=body, author_name=name, author_email=email, date=date )
        mail.save();
        email_notifier.new_mail(mail)
        return HttpResponseRedirect(reverse('index'))


def add_announce(request):
    # Here I should check if the informations are valid, but as they are already verified on the client side we are going to concider for this project that they are well formed
    try:
        token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
        title = request.POST['title']
        description = request.POST['description']
        name = request.POST['name']
        email = request.POST['email']
        date = timezone.now()
    except (KeyError):
        return HttpResponse("error")
    else:
        announce = Announce(title=title, description=description, author_name=name, author_email=email, edit_date=date, private_token=token )
        announce.save();
        email_notifier.announce_creation(announce)
        return HttpResponseRedirect(reverse('index'))


    return HttpResponse(token)
