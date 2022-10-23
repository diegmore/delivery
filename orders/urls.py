
from django.urls import include, re_path
from rest_framework import routers
from .views import OrderViewset


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', OrderViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]