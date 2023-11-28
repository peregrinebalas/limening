from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Create your models here.
class NlpModel(models.Model):
    source = models.CharField
    model_version = models.CharField

class Clade(models.Model):
    name = models.CharField(max_length=32)
    # sapience = models.CharField()

    def __str__(self):
        return self.name

class Portal(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    point = models.PointField(blank = True, null=True, srid=4326)

    def save(self, *args, **kwargs):
        self.point = Point(self.lng, self.lat)
        super(Wall, self).save(*args, **kwargs)

    def order_by_dist(point):
        return Portal.objects.annotate(distance=Distance('point', point))

    @property
    def animi(self):
        return self.animi_set.all().order_by('-manifested_at')

    def __str__(self):
        return self.name

# Animi personality fields:
# vert - how outgoing the animi is. visible to user.
# psyche projection - if the animi will take previous experiences from other users and approach a new user as though they will behave the same way. no visible to users.
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
    projection = models.BooleanField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manifested_at = models.DateTimeField
    portal = models.ForeignKey(Portal)

    def __str__(self):
        return self.name

