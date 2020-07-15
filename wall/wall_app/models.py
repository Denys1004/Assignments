from django.db import models
from log_reg_app.models import *

# Create your models here.
# class MessageManager(models.Manager):
#     def create_message(self, postData):
#         return self.create(message = postData['message'])


class Message(models.Model):
    message = models.CharField(max_length = 255)
    poster = models.ForeignKey('log_reg_app.User', related_name = 'messages', on_delete=models.CASCADE) # poster is User, we need to point to User with a foreign key # related name is a reverse look up: Message has a poster, User has messages
    created_at = models.DateTimeField(auto_now_add = True)  								
    updated_at = models.DateTimeField(auto_now = True)	
    # objects = MessageManager()

class Comment(models.Model):
    comment = models.CharField(max_length = 255)
    poster = models.ForeignKey('log_reg_app.User', related_name = 'comments', on_delete=models.CASCADE) # Comments has a poster, User has comments
    message = models.ForeignKey(Message, related_name = 'comments', on_delete=models.CASCADE) # message where comment was posted on. Message has comments, but comment belongs to one message 
    created_at = models.DateTimeField(auto_now_add = True)  								
    updated_at = models.DateTimeField(auto_now = True)	