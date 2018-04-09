from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
	url(r'^$', views.index),
	url(r'^time_display$', views.time_display)
	#url(r'^test$', views.test)     # This line has changed!
  ]