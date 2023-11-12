from django.db import models

# Create your models here.

class Limenling(models.Model):
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
    clade = models.ForeignKey(Clade)
    nlp_model = models.ForeignKey(NlpModel)
    max_speed = models.BigIntegerField
    vert = models.CharField(max_length=1, choices=VERT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Clade(models.Model):
    name = models.CharField(max_length=32)
    # sapience = models.

    def __str__(self):
        return self.name

class NlpModel(models.Model):
    