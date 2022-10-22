from django.db import models

# Create your models here.
class DeliveryMan(models.Model):
    lat = models.IntegerField()
    long = models.IntegerField()
    last_update = models.DateTimeField()