from django.db import models

# Create your models here.

class Limenling(model.Model):
    OMNIVERT = "O"
    AMBIVERT = "A"
    INTROVERT = "I"
    EXTROVERT = "E"
    VERT_CHOICES = [
        (OMNIVERT, "Omnivert"),
        (AMBIVERT, "Ambivert"),
        (INTROVERT, "Introvert"),
        (EXTROVERT, "extro")
    ]

    name = models.CharField(max_length=32)
    max_speed = models.BigIntegerField
    vert = models.CharField(max_length=1, choices=VERT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)