from django.db import models
from limening import Animi
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

class AnimiMessage(models.Model):
    message = models.ForeignKey(Message)
    animi = models.ForeignKey(Animi)
    is_response = models.BooleanField
    confidence_score = models.FloatField(max=1.0, min=0.0)

class UserMessage(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
