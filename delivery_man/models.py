from django.db import models

# Create your models here.
class DeliveryMan(models.Model):
    lat = models.IntegerField(default=0)
    long = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['last_update']