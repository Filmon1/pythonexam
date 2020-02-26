from django.urls import path
from .import views 

urlpatterns = [
    path("", views.index),
    path("signup",views.signup),
    path("login", views.login),
    path("travels", views.travelsdasboard),
    path("logout", views.userlogout), 
    path("travels/add", views.addingtraveler), 
    path("addatrip", views.addingtrip),
    path("jointrip/<tripId>", views.jointrip), 
    path("tripdetail/<tripId>", views.tripdetail)
]
