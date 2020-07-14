from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, "success.html", context)

# REGISTRATION
def create(request):
    errors = User.objects.validator(request.POST)	
    if len(errors)>0:													
        for value in errors.values():											
            messages.error(request, value)											
        return redirect('/')
    new_user = User.objects.register(request.POST)     # hash users password before storing it into db
    request.session['user_id'] = new_user.id
    return redirect('/success')

# LOGIN
def login(request):
    result = User.objects.authenticate(request.POST['email'],request.POST['password']) # Checking login
    if result == False:
        messages.error(request, "Email or passwort do not match.")
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/success')
    return redirect('/')

# LOGOUT
def logout(request):
    request.session.clear()
    return redirect("/")



