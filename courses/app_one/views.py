from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)


def process_form(request):
    errors = Course.objects.validator(request.POST)
    validate(request, errors)
    return redirect('/')


# VALIDATOR
def validate(request, errors):
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_course = Course.objects.create(
            name = request.POST['name'],
            description = request.POST['description']
            )

def destroy_or_cancel(request, id):
    context = {
        'current_course': Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def remove(request, id):
    cur_course = Course.objects.get(id=id)
    cur_course.delete()
    return redirect('/')