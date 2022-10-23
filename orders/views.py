from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from delivery_man.models import DeliveryMan
from rest_framework.response import Response

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        queryset = self.queryset.filter(delivery_date__contains=request.GET.get('orderedDate'))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)
    
    @action(
        methods=['get'],
        detail=False,
        url_path='get-orders-by-deliveryman',
        url_name='get-orders-by-deliveryman'
    )
    def get_orders_by_delivery_man(self, request):
        queryset = self.queryset.filter(delivery_date__contains=request.GET.get('orderedDate'),
                                        delivery_man=request.GET.get('deliveryMan'))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)
    
    @action(
        methods=['get'],
        detail=False,
        url_path='get-near-deliveryman',
        url_name='get-near-deliveryman'
    )
    def get_near_delivery_man(self, request):
        query_date = request.GET.get('queryDate')
        query_lat = int(request.GET.get('queryLat'))
        query_lng = int(request.GET.get('queryLng'))
        queryset = self.queryset.filter(delivery_date=query_date)
        deliver_id = None
        lat_distance = 100
        lng_distance = 100
        distance_sum = 200
        if queryset: 
            for order in queryset:
                order_lat_distance = abs(query_lat - order.destination_lat)
                order_long_distance = abs(query_lng - order.destination_long)
                order_distance_sum = order_lat_distance + order_long_distance
                if order_distance_sum < distance_sum:
                    distance_sum = order_distance_sum
                    deliver_id = order.delivery_man.id
                    lat_distance = order.destination_lat
                    lng_distance = order.destination_long
        return Response({'deliver_id':deliver_id, 'actual_lat':lat_distance, 'actual_lng':lng_distance}, 200)