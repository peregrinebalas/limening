from django.db import models
from limening import Limling
from users import User

# Create your models here.
class Conversation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField

class Message(models.Model):
    conversation = models.ForeignKey(Conversation)
    content = models.CharField
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class LimlingMessage(models.Model):
    message = models.ForeignKey(Message)
    limling = models.ForeignKey(Limling)
    is_response = models.BooleanField

class UserMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
