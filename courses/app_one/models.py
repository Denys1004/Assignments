from django.db import models


import re
# from datetime import date, datetime
# today = date.today()
# today = datetime(today.year, today.month, today.day)

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        name = self.filter(name = postData['name'])
        print("OOOOOOOOOOOOOOOO", name)
        if name:
            errors['name'] = 'Name allready exists.'
        if len(postData['name']) < 5:
            errors['name'] = 'Name should be atleast 5 characters.'
  
        if len(postData['description']) > 0 and len(postData['description']) < 15 :
            errors['description'] = 'Description should be atleast 15 characters.'

        return errors



class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)	
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()