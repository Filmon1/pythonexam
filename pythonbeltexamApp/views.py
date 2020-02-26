from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q


# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    errors = User.objects.formvalidator(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    HashedPW = bcrypt.hashpw(request.POST['Password'].encode(), bcrypt.gensalt()).decode()
    HashedcPW = bcrypt.hashpw(request.POST['confirmpw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstName = request.POST['firstname'], Username = request.POST['username'], passsword = HashedPW, confirmPW = HashedcPW)

    request.session['signedInUserID'] = newuser.id

    return redirect("/travels")

def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.filter(Username = request.POST['username'])
        user = user[0]
        request.session['signedInUserID'] = user.id
    return redirect("/travels")

def travelsdasboard(request):
    if 'signedInUserID' not in request.session:
        return redirect('/')
    userinfo = User.objects.get(id = request.session['signedInUserID'])

    context = {
        'users': userinfo,
        'mytrip': Destination.objects.filter(planner = userinfo) | Destination.objects.filter(joinedTraveler = userinfo ),
        'otherstrip':Destination.objects.exclude(Q(planner = userinfo) | Q(joinedTraveler= userinfo ))
    }
    return render(request, "hello.html", context)

def addingtraveler(request):
    if 'signedInUserID' not in request.session:
        return redirect('/')
    return render(request, "add.html")


def addingtrip(request):
    errors = Destination.objects.tripvalidator(request.POST)
    if request.POST['TravelDateFrom'] > request.POST['TravelDateTo']:
        errors['TravelDateFrom'] = "Invalid Date"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/travels/add')
    else:
        loggedinuser = User.objects.get(id = request.session['signedInUserID'])
        newtrip = Destination.objects.create(destination = request.POST['Destination'], description = request.POST['Description'], travel_start_date = request.POST['TravelDateFrom'], travel_End_Date = request.POST['TravelDateTo'], planner = loggedinuser)
        return redirect("/travels")

def jointrip(request, tripId):
    loggedinuser = User.objects.get(id = request.session['signedInUserID'])
    triptoadd = Destination.objects.get(id = tripId)
    loggedinuser.trip_joined.add(triptoadd)
    return redirect("/travels")

def tripdetail(request, tripId):
    tripdetail = Destination.objects.get(id = tripId)
    context = {
        'tripdetails': tripdetail
    }
    return render(request, "tripdetail.html", context)

def userlogout(request):
    request.session.clear()
    return redirect('/')

