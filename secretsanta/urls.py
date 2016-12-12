from django.conf.urls import url

from . import views

app_name = 'secretsanta'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details', views.details, name='details'),
    url(r'^check_person/(?P<person_id>[0-9]+)$', views.check_person, name='check_person'),
    url(r'^rematch/(?P<match_id>[0-9]+)$', views.rematch, name='rematch'),
]
