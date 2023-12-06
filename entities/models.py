from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

class NlpModel(models.Model):
    source = models.CharField
    model_version = models.CharField

# Family: (noun) A set of entities with common characteristics.
# The Family model defines generic behaviors of each entity type.
# When an entity is created, their "nature" is from their famiy,
# which is then built on by their individual experiences.
class Family(models.Model):
    BILATERAL = "B"
    RADIAL = "R"
    ASYMMETRICAL = "A"
    BODY_PLAN_CHOICES = [
        (BILATERAL, "Bilateral"),
        (RADIAL, "Radial"),
        (ASYMMETRICAL, "Asymmetrical")
    ]
    name = models.CharField(max_length=32)
    body_plan = models.CharField(choices=BODY_PLAN_CHOICES)
    base_form = models.ImageField
    max_speed = models.BigIntegerField
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
        super(Portal, self).save(*args, **kwargs)

    def order_by_dist(point):
        return Portal.objects.annotate(distance=Distance('point', point))

    @property
    def entity(self):
        return self.entity_set.all().order_by('-manifested_at')

    def __str__(self):
        return self.name

# Entity: (noun) a thing with distinct and independent existence.

class Entity(models.Model):
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
    family = models.ForeignKey(Family)
    nlp_model = models.ForeignKey(NlpModel)
    max_speed = models.BigIntegerField
    vert = models.CharField(max_length=1, choices=VERT_CHOICES) # how outgoing the entity is. visible to user.
    projection = models.BooleanField # if the entity will take previous experiences from other users and approach a new user as though they will behave the same way. not visible to users.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manifested_at = models.DateTimeField
    portal = models.ForeignKey(Portal)

    def __str__(self):
        return self.name

