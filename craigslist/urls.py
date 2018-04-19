from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<announce_id>[0-9]+)/$', views.announce_detail, name='announce_detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^add/$', views.add_announce, name='add_announce'),

]
