# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^home$', views.home),
#     url(r'^register$', views.register),
#     url(r'^login$', views.login),
#     url(r'^logout$', views.logout),
#     url(r'^add$', views.add),
#     url(r'^create_trip$', views.create_trip),
#     url(r'^trip/(?P<id>\d+)$', views.tripInfo),
#     url(r'^join/(?P<id>\d+)$', views.join_trip),
# ]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^create_trip$', views.create_trip),
    url(r'^trip/(?P<id>\d+)$', views.tripInfo),
    url(r'^join/(?P<id>\d+)$', views.join_trip),
]