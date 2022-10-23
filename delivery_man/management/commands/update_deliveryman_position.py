from django.core.management.base import BaseCommand, CommandError
import requests
from django.db import transaction
from delivery_man.models import DeliveryMan

DELIVERYMAN_REQUEST_URL = 'https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json'

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        deliveryman_positions_request = requests.get(DELIVERYMAN_REQUEST_URL)
        if deliveryman_positions_request.status_code != 200:
            raise CommandError('Error trying to request the delivery man positions')
        deliveryman_data = deliveryman_positions_request.json().get('alfreds', [])
        with transaction.atomic():
            for deliveryman in deliveryman_data:
                deliveryman_object = DeliveryMan.objects.get_or_create(id=deliveryman.get('id'))
                print(deliveryman_object)
                print(asdas)
            