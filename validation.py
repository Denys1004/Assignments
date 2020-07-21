# models.py:
from django.db import models
import re
from datetime import date, datetime

today = date.today()
today = datetime(today.year, today.month, today.day)

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if 'id' not in postData:  #Creating. if id not exists, that means we creating object
            if self.filter(title = postData['title']): #array with objects with this title
                errors['title'] = 'Title allready exists.'
        else:
            # Editing. if the title they are trying to change this show's title to already exists BUT the title is not the original title of that show
            if self.filter(title = postData['title'] and Show.objects.get(id=postData['id']).title != postData['title']):
                errors['title'] = 'Title allready exists.'

        if len(postData['title']) < 1:
            errors['title'] = 'Title field required.'
        if len(postData['network']) < 1:
            errors['network'] = 'Network field required.'
        if len(postData['release_date']) < 1:
            errors['release_date'] = 'Release date field required.'
        
        datetime_str = postData['release_date']
        datetime_str = datetime.strptime(datetime_str, '%Y-%m-%d')
        if datetime_str > today:
            errors['release_date'] = 'Release date must be in the past.'
        
        if len(postData['description']) > 0 and len(postData['description']) < 11 :
            errors['description'] = 'Description should be atleast 10 characters.'
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)	
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

# views.py: 
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

# html:
{% if messages %}                                                               		
<ul class="messages">  										  	
    {% for message in messages %}    									
        <li class="errors">{{ message }}</li>   	
    {% endfor %}												
</ul>														
{% endif %}	