from django.db import models

# Create your models here.
class NlpModel(models.Model):
    source = models.CharField
    model_version = models.CharField

class Clade(models.Model):
    name = models.CharField(max_length=32)
    # sapience = models.CharField()

    def __str__(self):
        return self.name

class Animi(models.Model):
    OMNIVERT = "O"
    AMBIVERT = "A"
    INTROVERT = "I"
    EXTROVERT = "E"
    VERT_CHOICES = [
        (OMNIVERT, "Omnivert"),
        (AMBIVERT, "Ambivert"),
        (INTROVERT, "Introvert"),
        (EXTROVERT, "Extrovert")
    ]

    name = models.CharField(max_length=32)
    clade = models.ForeignKey(Clade)
    nlp_model = models.ForeignKey(NlpModel)
    max_speed = models.BigIntegerField
    vert = models.CharField(max_length=1, choices=VERT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
