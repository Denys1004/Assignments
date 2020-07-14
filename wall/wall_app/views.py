from django.shortcuts import render, redirect

# Create your views here.
def wall(request):
    return render(request, 'wall.html')
