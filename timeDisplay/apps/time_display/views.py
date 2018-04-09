from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
	context = {
	"dateTime": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	return render(request,'time_display/index.html', context)
def time_display(request):
	context = {
	"dateTime": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	return render(request,'time_display/index.html', context)