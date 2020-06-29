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
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if request.POST['location'] == 'farm':
        num = random.randint(10, 20)
        request.session["your_gold"] += num
        request.session['activities'].append([f"Earned {num} gold from the farm! ({current_time})", 'green'])
    elif request.POST['location'] == 'cave':
        num = random.randint(5, 10)
        request.session["your_gold"] += num
        request.session['activities'].append([f"Earned {num} gold from the cave! ({current_time})", 'green'])
    elif request.POST['location'] == 'house':
        num = random.randint(2, 5)
        request.session["your_gold"] += num
        request.session['activities'].append([f"Earned {num} gold from the house! ({current_time})", 'green'])
    elif request.POST['location'] == 'casino':
        chance = random.randint(1, 2)
        num = random.randint(0, 50)
        if chance == 1:
            request.session["your_gold"] += num
            request.session['activities'].append([f"Earned {num} gold from the casino! ({current_time})", 'green'])
        else:
            request.session["your_gold"] -= num
            request.session['activities'].append([f"Lost {num} gold from the casino! ({current_time})", 'red'])
    return redirect('/')