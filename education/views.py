from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from django.core.management import call_command


# Create your views here.
current_year = call_command("current_year")
def land(request):
    context = {
        "year" : current_year
    }
    
    return render(request, "home.html", context)    
    # return HttpResponse('')

def joinus(request):
    return render(request, "joinus.html")

def aboutus(request):
    return HttpResponse("This is about us")

def contactus(request):
    return HttpResponse("This is contact us")

def loginuser(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)

            # check if user has entered correct credentials
            user = authenticate(email=username, password=password)
            print(user)

            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/course")
            elif user is None:
                print('Invalid')
            else:
                # No backend authenticated the credentials
                return render(request, 'login.html')

        return render(request, 'login.html')
    elif User.is_authenticated:
        return redirect("course")

def logoutuser(request):
    if User.is_authenticated:
        logout(request)
    else:
        return redirect("/")

def signin(request):
    return render(request, "sign_in.html")

def startthecourse(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "starter.html")
