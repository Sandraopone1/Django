from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
import bcrypt

def index(request):
    return render(request, 'new_project/index.html')
# def update(request):
#     errors = Blog.objects.basic_validator(request.POST)
#         if len(errors):
#             for tag, error in errors.iteritems():
#                 messages.error(request, error, extra_tags=tag)
#             return redirect('/blog/edit/'+id)
#         else:
#             blog = Blog.objects.get(id = id)
#             blog.name = request.POST['name']
#             blog.desc = request.POST['desc']
#             blog.save()
#             return redirect('/blogs')
def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.create(
        name=request.POST['name'],
        username=request.POST['username'],
        password=bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
        )
    request.session["user_id"] = user.id
    return redirect('/home')
def login(request):
    user = User.objects.login_validator(request.POST)
    if user["is_valid"]:
        request.session["user_id"] = user["user"].id
        return redirect('/home')
    else:
        for error in user["errors"]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')
def home(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "tripsbyme": Trip.objects.filter(plannedby=request.session['user_id']),
        "tripsbyothers": Trip.objects.exclude(plannedby=request.session['user_id'])
        }

    return render(request, 'new_project/home.html', context)

def add(request):
    return render(request, 'new_project/add.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def createAtrip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    else:
        the_trip = Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            startdate = request.POST['startdate'],
            enddate = request.POST['enddate'],
            plannedby = User.objects.get(id=request.session['user_id']),
            )
        trip_plan = schedules.objects.create(
            the_trip = Trip.objects.last(),
            the_traveller = User.objects.get(id=request.session['user_id'])
        )
    return redirect('/home')

def infoAbouttrip(request, id):
    context = {
        'the_trip': Trip.objects.get(id=id),
        'the_travellers': schedules.objects.filter(the_trip=Trip.objects.get(id=id))
    }

    return render(request,'new_project/tripsummary.html', context)
def joinTrip(request, id):
    the_plan = schedules.objects.create(
        the_trip = Trip.objects.get(id=id),
        the_traveller= User.objects.get(id=request.session['user_id'])
    )
    return redirect('/trip/'+ id)

