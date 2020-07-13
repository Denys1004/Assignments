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
    return render(request, "success.html")

def registration(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)										
        if len(errors)>0:													
            for value in errors.values():											
                messages.error(request, value)											
            return redirect('/')									
        else:
            if request.POST['first_name'] not in request.session:
                request.session["name"] = request.POST['first_name']
            password = request.POST['password']										
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() # create the hash 
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], birth_date=request.POST['birth_date'], email=request.POST['email'], password=pw_hash)
            return redirect("/success") # never render on a post, always redirect!  																	
    return redirect("/")


def login(request):
    results = User.objects.filter(email=request.POST['email'])
    if len(results) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), results[0].password.encode()) and results[0].email == request.POST['email']:
            request.session['user_id'] = results[0].id
            request.session["name"] = results[0].first_name
            return redirect('/success')
        else:
            messages.error(request, "Email or passwort did not match.")
            return redirect("/")
    else:
        messages.error(request, "Email or passwort did not match.")
        return redirect("/")
            

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect("/")



