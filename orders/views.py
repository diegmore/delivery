from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer