from django.db import models
import re 
import bcrypt 
import datetime



class formManager(models.Manager):
    def formvalidator(self, postData):
        errors = {}
        if len(postData['firstname']) < 1:
            errors['firstnamerequired'] = "First name cannot be empty"
        elif len(postData['firstname']) < 3:
            errors['shortfirst name'] = "first name too short. first name cannot be less than 3 characters"
        if len(postData['username']) < 1:
            errors['Username'] = "username cannot be empty"
        elif len(postData ['username']) < 3:
            errors['shortUsername'] = " Username too short. Network cannot be least than 3 characters"
        if len(postData['Password']) < 8:
            errors['shortPassword'] = " Password cannot be less than 8 characters"
        if len(postData['Password']) != len(postData['confirmpw']):
            errors['matchingpasswords'] = "Password don't Match"
        UsernamealradyInUse = User.objects.filter(Username = postData['username'])
        if len(UsernamealradyInUse) > 0:
            errors['usernamexits'] = "Username already exists, Please use a different Username"
        return errors
    
    def loginvalidator(self, postData):
        errors = {}
        if len(postData['username']) < 1:
            errors['username'] = "username cannot be empty"
        exsitinguser = User.objects.filter(Username = postData['username'])
        if len(exsitinguser) == 0:
            errors['userexist'] = "Username not found, Please register"
        else:
            if bcrypt.checkpw(postData['Password'].encode(), exsitinguser[0].passsword.encode()):
                print('password matches')
            else:
                errors['passwordmismatch'] = 'password donnot match'
        return errors 

class tripManager(models.Manager):
    def tripvalidator(request, postData):
        errors = {}
        present = datetime.date.today()
        traveldate = datetime.datetime.strptime(postData['TravelDateFrom'], "%Y-%m-%d").date()
        if len(postData['Destination']) < 1:
            errors['Destination'] = "Destination cannot be empty"
        if len(postData['Description']) < 1:
            errors['Description'] = "Description cannot be empty"
        if len(postData['TravelDateFrom']) < 1:
            errors['TravelDateFrom'] = "Travel Date From cannot be empty"
        if traveldate < present:
            errors['TravelDateFrom'] = "Date from has to be from the future"
        if len(postData['TravelDateTo']) < 1: 
             errors['TravelDateTo'] = "Travel Date To cannot be empty"
        return errors 
            



# Create your models here.



class User(models.Model):
    firstName = models.CharField(max_length = 255)
    Username = models.CharField(max_length = 255)
    passsword = models.CharField(max_length = 255)
    confirmPW = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = formManager()
    
    


class Destination(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.TextField()
    travel_start_date = models.DateField()
    travel_End_Date = models.DateField()
    planner = models.ForeignKey(User, related_name= "destinations", on_delete = models.CASCADE)
    joinedTraveler = models.ManyToManyField(User, related_name ="trip_joined")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = tripManager()


    




