from django.shortcuts import render, redirect
from apps.log_reg_app.models import *
from .models import *
from django.contrib import messages
import datetime
from datetime import timedelta # to find old if message older then 30 minutes

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'all_messages': Message.objects.all().order_by('-created_at'),
        'users' : User.objects.all(),
        'cur_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'wall.html', context)


def create_message(request):
    if request.method == "POST":
        message = Message.objects.create(message = request.POST['message'], poster = User.objects.get(id = request.session['user_id']))
    return redirect('/wall')


def add_comment(request, id):
    if request.method == "POST":
        new_comment = Comment.objects.create(comment = request.POST['comment'], poster = User.objects.get(id = request.session['user_id']), message = Message.objects.get(id = id))
        return redirect('/wall')
    return redirect('/wall')

def add_like(request, id):
    user_liking = User.objects.get(id = request.session['user_id'])
    message_liked = Message.objects.get(id = id)
    message_liked.likes.add(user_liking)
    return redirect('/wall')

def delete_message(request, id):
    message_to_delete = Message.objects.get(id=id)
    posted_time = message_to_delete.created_at
    current_time = datetime.datetime.now()
    # datetime.datetime.now() - datetime.timedelta(minutes=30)
    if message_to_delete.poster.id == request.session['user_id']:
        message_to_delete.delete()
    else:
        messages.warning(request, 'You may delete only your own messages')



    return redirect('/wall')

def delete_user(request, id):
    user_to_delete = User.objects.get(id = id)
    user_to_delete.delete()
    return redirect('/wall')