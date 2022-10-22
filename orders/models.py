from django.db import models

# Create your models here.
class Order(models.Model):
    delivery_date = models.DateTimeField()
    delivery_lat = models.IntegerField()
    delivery_long = models.IntegerField()
    destination_lat = models.IntegerField()
    destination_long = models.IntegerField()
    