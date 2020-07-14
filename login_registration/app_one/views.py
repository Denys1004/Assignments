from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)


def success(request):
    return render(request, "success.html")

def registration(request):
    errors = User.objects.validator(request.POST)	
    if len(errors)>0:													
        for value in errors.values():											
            messages.error(request, value)											
        return redirect('/')
    # hash users password before storing it into db
    User.objects.register(request.POST)
    return redirect('/success')


def login(request):
    result = User.objects.authenticate(request.POST['email'],request.POST['password']) # Checking login
    if result == False:
        messages.error(request, "Email or passwort do not match.")
    else:
        return redirect('/success')

            

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect("/")



