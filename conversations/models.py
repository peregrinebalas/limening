from django.db import models

# Create your models here.
class Conversation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField

class Message(models.Model):
    conversation = models.ForeignKey(Conversation)
    content = models.CharField
    created = models.DateTimeField(auto_now_add=True)

class LimenlingMessage(models.Model):
    message = models.ForeignKey(Message)
    limenling = models.ForeignKey(Limenling)
    is_response = models.BooleanField

class UserMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)


