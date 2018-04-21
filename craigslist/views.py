from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

from . import email_notifier


from .models import Announce, Mail, MailForm, AnnounceForm

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

def send_mail(request):
    mail = MailForm(request.POST)
    email_notifier.new_mail(mail.save())
    return HttpResponseRedirect(reverse('index'))

def edit(request, announce_id):
    announce = get_object_or_404(Announce, pk=announce_id)
    try:
        key = request.GET['key']
        if ( key != announce.private_token):
            return HttpResponseRedirect(reverse('index'))
    except (KeyError):
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'craigslist/edit.html', {'announce': announce})

def delete(request, announce_id):
    announce = get_object_or_404(Announce, pk=announce_id)
    try:
        private_token = request.GET['key']
    except (KeyError):
        return HttpResponse("error")
    if ( private_token == announce.private_token):
        announce.delete()
    return HttpResponseRedirect(reverse('index'))


def edit_save(request, announce_id):
    # Here I should check if the informations are valid, but as they are already verified on the client side we are going to concider for this project that they are well formed
    # I could have done that using ModelForm
    announce = get_object_or_404(Announce, pk=announce_id)
    try:
        title = request.POST['title']
        description = request.POST['description']
        private_token = request.POST['private_token']
        date = timezone.now()
    except (KeyError):
        return HttpResponse("error")
    else:
        if ( private_token == announce.private_token):
            announce.title = title
            announce.description = description
            announce.edit_date = date
            announce.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("error")



def add_announce(request):
    announce = AnnounceForm(request.POST)
    email_notifier.announce_creation(announce.save())
    return HttpResponseRedirect(reverse('index'))
