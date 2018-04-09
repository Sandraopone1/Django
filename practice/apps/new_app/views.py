# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib import messages
# from models import *
# import bcrypt

# def index(request):
#     return render(request, 'new_app/index.html')

# def home(request):
#     data = {
#         "user": User.objects.get(id=request.session['user_id']),
#         "my_trips": Trip.objects.filter(planned_by=request.session['user_id']),
#         "other_trips": Trip.objects.exclude(planned_by=request.session['user_id'])
#         }

#     return render(request, 'new_app/home.html', data)

# # def update(request):
# #     errors = Blog.objects.basic_validator(request.POST)
# #         if len(errors):
# #             for tag, error in errors.iteritems():
# #                 messages.error(request, error, extra_tags=tag)
# #             return redirect('/blog/edit/'+id)
# #         else:
# #             blog = Blog.objects.get(id = id)
# #             blog.name = request.POST['name']
# #             blog.desc = request.POST['desc']
# #             blog.save()
# #             return redirect('/blogs')
# def register(request):
#     # check for
#     errors = User.objects.register_validator(request.POST)
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/')
#         #if no error register user
#     else:

#         user = User.objects.create(    
#         name = request.POST['name'],
#         username = request.POST['username'],
#         password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()),
#         )
#     request.session["user_id"] = user.id
#     return redirect('/home')

# def login(request):
#     user = User.objects.login_validator(request.POST)
#     if user["is_valid"]:
#         request.session["user_id"] = user["user"].id
#         return redirect('/home')
#     else:
#         for error in user["errors"]:
#             messages.add_message(request, messages.ERROR, error)
#     return redirect('/')

# def logout(request):
#     request.session.clear()
#     return redirect('/')

# def add(request):
#     return render(request, 'new_app/add.html')

# def create_trip(request):
#     errors = Trip.objects.trip_validator(request.POST)
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/add')
#     else:
#         trip = Trip.objects.create(
#             destination = request.POST['destination'],
#             description = request.POST['description'],
#             start_date = request.POST['start_date'],
#             end_date = request.POST['end_date'],
#             planned_by = User.objects.get(id=request.session['user_id']),
#             )
#         plan = Plans.objects.create(
#             trip = Trip.objects.last(),
#             traveller = User.objects.get(id=request.session['user_id'])
#         )
#     return redirect('/home')

# def tripInfo(request, id):
#     data = {
#         'trip': Trip.objects.get(id=id),
#         'travellers': Plans.objects.filter(trip=Trip.objects.get(id=id))
#     }

#     return render(request,'new_app/tripInfo.html', data)

# def join_trip(request, id):
#     plan = Plans.objects.create(
#         trip = Trip.objects.get(id=id),
#         traveller= User.objects.get(id=request.session['user_id'])
#     )
#     return redirect('/trip/'+ id)

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
import bcrypt

def index(request):
    return render(request, 'new_app/index.html')

def home(request):
    data = {
        "user": User.objects.get(id=request.session['user_id']),
        "my_trips": Trip.objects.filter(planned_by=request.session['user_id']),
        "other_trips": Trip.objects.exclude(planned_by=request.session['user_id'])
        }

    return render(request, 'new_app/home.html', data)

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

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request):
    return render(request, 'new_app/add.html')

def create_trip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    else:
        trip = Trip.objects.create(
            destination = request.POST['destination'],
            description = request.POST['description'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            planned_by = User.objects.get(id=request.session['user_id']),
            )
        plan = Plans.objects.create(
            trip = Trip.objects.last(),
            traveller = User.objects.get(id=request.session['user_id'])
        )
    return redirect('/home')

def tripInfo(request, id):
    data = {
        'trip': Trip.objects.get(id=id),
        'travellers': Plans.objects.filter(trip=Trip.objects.get(id=id))
    }

    return render(request,'new_app/tripInfo.html', data)

def join_trip(request, id):
    plan = Plans.objects.create(
        trip = Trip.objects.get(id=id),
        traveller= User.objects.get(id=request.session['user_id'])
    )
    return redirect('/trip/'+ id)
