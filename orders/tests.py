
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
        Order.objects.create(
            **data, delivery_man=DeliveryMan.objects.all().last())
        data.update({'delivery_man': DeliveryMan.objects.all().last().id})
        # when
        url = reverse('order-list')
        response = self.client.post(url, data, format='json')
        # then
        self.assertEqual(response.json(), {'non_field_errors': [
                         'This delivery man already has a order at this time']})

    def test_get_all_orders(self):
        # given
        data = {
            "delivery_date": "2022-10-22T20:05:00.000Z",
            "delivery_lat": 1,
            "delivery_long": 1,
            "destination_lat": 50,
            "destination_long": 50
        }
        Order.objects.create(
            **data, delivery_man=DeliveryMan.objects.all().last())
        # when
        url = reverse('order-list')
        response = self.client.get(url, {'orderedDate': '2022-10-22'})
        # then
        self.assertEqual(response.json(), [{'id': 3, 'delivery_man': 3, 'delivery_date': '2022-10-22T20:05:00Z',
                         'delivery_lat': 1, 'delivery_long': 1, 'destination_lat': 50, 'destination_long': 50}])

    def test_get_all_orders_by_delivery_man(self):
        # given
        data = {
            "delivery_date": "2022-10-22T20:05:00.000Z",
            "delivery_lat": 1,
            "delivery_long": 1,
            "destination_lat": 50,
            "destination_long": 50
        }
        Order.objects.create(
            **data, delivery_man=DeliveryMan.objects.all().last())
        # when
        url = reverse('order-get-orders-by-deliveryman')
        response = self.client.get(
            url, {'orderedDate': '2022-10-22', 'deliveryMan': 4})
        # then
        self.assertEqual(response.json(), [{'id': 4, 'delivery_man': 4, 'delivery_date': '2022-10-22T20:05:00Z',
                         'delivery_lat': 1, 'delivery_long': 1, 'destination_lat': 50, 'destination_long': 50}])

    def test_get_nearest_delivery_man(self):
        # given
        data = {
            "delivery_date": "2022-10-22T20:05:00.000Z",
            "delivery_lat": 1,
            "delivery_long": 1,
            "destination_lat": 50,
            "destination_long": 50
        }
        Order.objects.create(
            **data, delivery_man=DeliveryMan.objects.all().last())
        # when
        url = reverse('order-get-near-deliveryman')
        response = self.client.get(
            url, {'queryDate': '2022-10-22T20:05:00.000', 'queryLat': 51, 'queryLng': 51})
        # then
        self.assertEqual(response.json(), {
                         'deliver_id': 5, 'actual_lat': 50, 'actual_lng': 50})
