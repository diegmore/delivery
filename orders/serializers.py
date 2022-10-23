from rest_framework import serializers
from .models import Order
from datetime import timedelta


class OrderSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        added_datetime = attrs.get('delivery_date') + timedelta(hours=1)
        if Order.objects.filter(delivery_man = attrs.get('delivery_man').id, 
                                delivery_date__gte=attrs.get('delivery_date'),
                                delivery_date__lt=added_datetime):
            raise serializers.ValidationError('This delivery man already has a order at this time')
        return attrs
    
    class Meta:
        model = Order
        fields = ('id','delivery_man','delivery_date','delivery_lat','delivery_long','destination_lat','destination_long',)