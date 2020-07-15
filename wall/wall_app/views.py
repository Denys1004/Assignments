from django.shortcuts import render, redirect
from log_reg_app.models import *
from . models import *

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'all_messages': Message.objects.all(),
        'users' : User.objects.all(),
        'cur_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'wall.html', context)


def create_message(request):
    # if request.method == "POST":
    #     message = Message.objects.create(message = request.POST['message'], poster = User.objects.get(id = request.session['user_id']))
    print("YOUR FUCKING MESSAGE")
    return redirect('/wall')

def banana(request):
    # if request.method == "POST":
    #     message = Message.objects.create(message = request.POST['message'], poster = User.objects.get(id = request.session['user_id']))
    print("YOUR FUCKING MESSAGE")
    return redirect('/')
