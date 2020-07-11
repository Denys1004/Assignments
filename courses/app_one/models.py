from django.db import models


import re
# from datetime import date, datetime
# today = date.today()
# today = datetime(today.year, today.month, today.day)

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        name = self.filter(name = postData['name'])
        if name:
            errors['name'] = 'Name allready exists.'
        if len(postData['name']) < 5:
            errors['name'] = 'Name should be atleast 5 characters.'
  
        if len(postData['description']) > 0 and len(postData['description']) < 15 :
            errors['description'] = 'Description should be atleast 15 characters.'

        return errors

class CommentManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)	
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)	
    updated_at = models.DateTimeField(auto_now = True)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    objects = CommentManager()