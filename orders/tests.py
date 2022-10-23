
from rest_framework.test import APITestCase
from delivery_man.models import DeliveryMan
from django.urls import reverse
from .models import Order
# Create your tests here.


class CompanyTests(APITestCase):

    def setUp(self):
        DeliveryMan.objects.create(lat=1, long=1)

    def test_create_order(self):
        # given
        data = {
            "delivery_man": DeliveryMan.objects.all().last().id,
            "delivery_date": "2022-10-22T20:05:00.000Z",
            "delivery_lat": 1,
            "delivery_long": 1,
            "destination_lat": 50,
            "destination_long": 50
        }
        # when
        url = reverse('order-list')
        response = self.client.post(url, data, format='json')
        # then
        self.assertEqual(response.data, {'id': 1, 'delivery_man': 1, 'delivery_date': '2022-10-22T20:05:00Z',
                         'delivery_lat': 1, 'delivery_long': 1, 'destination_lat': 50, 'destination_long': 50})

    def test_fail_create_order(self):
        # given
        data = {
            "delivery_date": "2022-10-22T20:05:00.000Z",
            "delivery_lat": 1,
            "delivery_long": 1,
            "destination_lat": 50,
            "destination_long": 50
        }
        Order.objects.create(**data, delivery_man=DeliveryMan.objects.all().last())
        data.update({'delivery_man': DeliveryMan.objects.all().last().id})
        # when
        url = reverse('order-list')
        response = self.client.post(url, data, format='json')
        # then
        self.assertEqual(response.json(), {'non_field_errors': ['This delivery man already has a order at this time']})
