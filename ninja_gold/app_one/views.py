from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    curr_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if request.POST['location'] == 'farm':
        num = random.randint(10, 20)
        request.session['your_gold'] += num



    print(request.POST)
    return redirect('/')