from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import bcrypt



# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        
        if len(postData['name']) < 1:
            errors['name'] = "Name is required"
        elif len(postData['name']) < 2:
            errors['name'] = "name must be 2 or more characters"
        
        if len(postData['username']) < 1:
            errors['username'] = "Username is required"
        elif len(postData['username']) < 2:
            errors['username'] = "username must be 2 or more characters"

        if len(postData['password']) < 1:
            errors['password'] = "Password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be 8 characters or more"
        
        if len(postData["confirm"]) < 1:
            errors['confirm'] = "Confirm password is required"
        elif postData["password"] != postData["confirm"]:
            errors['confirm'] = "Confirm password must match Password"
            
        return errors
    def login_validator(self, postData):
        response = {
            "errors": [],
            "is_valid": True,
            "user": None
        }

        if len(postData['username']) < 1:
            response['errors'].append("Username is required")
        elif len(postData['username']) < 3:
            response['errors'].append("Username must have be at least 3 characters long")
        else:
            list_of_matching_username = User.objects.filter(username=postData['username'])
            if len(list_of_matching_username) == 0:
                response['errors'].append("Username not registered")
        
        if len(postData['password']) < 1:
            response['errors'].append("Password is required")
        elif len(postData['password']) < 8:
            response['errors'].append("Password must be at least 8 characters long")
        else:
            user = list_of_matching_username[0]
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                response['user'] = user
            else:
                response['errors'].append("Incorrect password")
        
        if len(response["errors"]) > 0:
            response["is_valid"] = False
        
        return response


        # if len(postData['username']) < 1:
        #     response['errors'].append("Username is required")
        # elif len(postData['username']) < 2:
        #     response['errors'].append("username must be 2 or more characters")
        # else:
        #     all_matching_username = User.objects.filter(username=postData['username'])
        #     if len(all_matching_username) == 0:
        #         response['errors'].append("The Username does not exist")
        
        # if len(postData['password']) < 1:
        #     response['errors'].append("Password is required")
        # elif len(postData['password']) < 8:
        #     response['errors'].append("Password must be at least 8 characters long")
        # else:
        #     user = all_matching_username[0]
        #     if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
        #         response['user'] = user
        #     else:
        #         response['errors'].append("Incorrect password")
        
        # if len(response["errors"]) > 0:
        #     response["valid"] = False
        
        # return response
    
class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        
        if len(postData['destination']) < 1:
            errors['destination'] = "destination is required"
        elif len(postData['destination']) < 2:
            errors['destination'] = "destination must be 2 or more characters"
        
        if len(postData['description']) < 1:
            errors['description'] = "description is required"
        elif len(postData['description']) < 2:
            errors['description'] = "description must be 2 or more characters"
        
        if len(postData['startdate']) < 1:
            errors['startdate'] = "Start date is required"
        else:
            startDate = datetime.strptime(postData["startdate"], "%Y-%m-%d")
            if startDate < datetime.now():
                errors['startdate'] = "Start date must be in the future and not in the past"
        
        if len(postData['enddate']) < 1:
            errors['enddate'] = "End date is required"
        else:
            endDate = datetime.strptime(postData["enddate"], "%Y-%m-%d")
            if endDate < startDate:
                errors['enddate'] = "End date cannot be before Start Date"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    plannedby = models.ForeignKey(User)
    objects = TripManager()

class schedules(models.Model):
    the_trip = models.ForeignKey(Trip)
    the_traveller = models.ForeignKey(User)


