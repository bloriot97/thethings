from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader


from .models import Announce

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
