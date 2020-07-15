from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "welcome.html")

def success(request):
    return redirect('/wall')

# REGISTRATION
def create(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        errors = User.objects.validator(request.POST)	
        if len(errors)>0:													
            for value in errors.values():											
                messages.error(request, value)											
            return redirect('/register')
        new_user = User.objects.register(request.POST)     # hash users password before storing it into db
        request.session['user_id'] = new_user.id
        return redirect('/wall')

# LOGIN
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        result = User.objects.authenticate(request.POST['email'],request.POST['password']) # Checking login
        if result == False:
            messages.error(request, "Email or passwort do not match.")
        else:
            user = User.objects.get(email = request.POST['email'])
            request.session['user_id'] = user.id
            return redirect('/wall')
        return redirect('/login')

# LOGOUT
def logout(request):
    request.session.clear()
    return redirect("/login")



