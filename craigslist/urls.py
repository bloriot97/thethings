from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<announce_id>[0-9]+)/contact/$', views.contact, name='contact'),
    url(r'^(?P<announce_id>[0-9]+)/send_mail/$', views.send_mail, name='send_mail'),
    url(r'^(?P<announce_id>[0-9]+)/$', views.announce_detail, name='announce_detail'),
    url(r'^(?P<announce_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<announce_id>[0-9]+)/edit_save/$', views.edit_save, name='edit_save'),
    url(r'^(?P<announce_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^new/$', views.new, name='new'),
    url(r'^add/$', views.add_announce, name='add_announce'),
]
