from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def add_new_show(request):
    return render(request, 'add_new_show.html')


def process_new_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'])
        return redirect('/shows')

def show_one_tvshow(request, id):
    num_id = int(id)
    context = {
        'needed_tv_show':Show.objects.get(id = num_id)
    } 
    return render(request, 'tv_show.html', context)

def edit(request, id):
    context = {
        'needed_tv_show':Show.objects.get(id = id)
    } 
    return render(request, 'edit.html', context) 

def update(request):
    errors = Show.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{request.POST["id"]}')
    else:
        edited_show = Show.objects.get(id = request.POST['id'])
        edited_show.title = request.POST['title']
        edited_show.network = request.POST['network']
        edited_show.release_date = request.POST['release_date']
        edited_show.description = request.POST['description']
        edited_show.save()
        return redirect('/shows')


def delete(request, id):
    num_id = int(id)
    needed_show = Show.objects.get(id = num_id)
    needed_show.delete()

    return redirect('/shows') 











