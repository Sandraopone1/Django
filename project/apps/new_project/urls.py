from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
    url(r'^createAtrip$', views.createAtrip),
    url(r'^trip/(?P<id>\d+)$', views.infoAbouttrip),
    url(r'^join/(?P<id>\d+)$', views.joinTrip),
]