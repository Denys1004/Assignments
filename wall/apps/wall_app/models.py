from django.db import models
from apps.log_reg_app.models import *


class Message(models.Model):
    message = models.TextField(default = 'Hello')
    poster = models.ForeignKey(User, related_name = 'messages', on_delete=models.CASCADE) # poster is User, we need to point to User with a foreign key # related name is a reverse look up: Message has a poster, User has messages
    likes = models.ManyToManyField(User, related_name = 'messages_liked')
    created_at = models.DateTimeField(auto_now_add = True)  								
    updated_at = models.DateTimeField(auto_now = True)	

class Comment(models.Model):
    comment = models.TextField(default = 'Hello')
    poster = models.ForeignKey(User, related_name = 'comments', on_delete=models.CASCADE) # Comments has a poster, User has comments
    message = models.ForeignKey(Message, related_name = 'comments', on_delete=models.CASCADE) # message where comment was posted on. Message has comments, but comment belongs to one message 
    created_at = models.DateTimeField(auto_now_add = True)  								
    updated_at = models.DateTimeField(auto_now = True)	