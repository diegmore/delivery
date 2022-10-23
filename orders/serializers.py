from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id','delivery_man','delivery_date','delivery_lat','delivery_long','destination_lat','destination_long',)