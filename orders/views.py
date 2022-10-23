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
        url_path='get-orders_by_deliveryman',
        url_name='get-orders_by_deliveryman'
    )
    def get_orders_by_delivery_man(self, request):
        queryset = self.queryset.filter(delivery_date__contains=request.GET.get('orderedDate'),
                                        delivery_man=request.GET.get('deliveryMan'))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)