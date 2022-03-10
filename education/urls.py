from django.contrib import admin
from django.urls import path
from education import views

urlpatterns = [
    path('', views.land, name="home"),
    path("join_us", views.joinus, name="joinus"),
    path("about_us", views.aboutus, name="aboutus"),
    path("contact_us", views.contactus, name="contactus"),
    path("login", views.loginuser, name="login"),
    path("logout", views.logoutuser, name="logout"),
    path("sign_in", views.signin, name="signin"),
    path("course", views.startthecourse, name="course")
]
