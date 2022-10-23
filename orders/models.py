from django.db import models
from delivery_man.models import DeliveryMan
# Create your models here.
class Order(models.Model):
    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    delivery_lat = models.IntegerField()
    delivery_long = models.IntegerField()
    destination_lat = models.IntegerField()
    destination_long = models.IntegerField()
    