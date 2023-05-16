from django.shortcuts import render
from rest_framework import routers, viewsets
from pinger.serializers import PingerSerializer
from pinger.models import Pings
# Create your views here.

class PingerViewSet(viewsets.ModelViewSet):

    queryset = Pings.objects.all()
    serializer_class = PingerSerializer

router = routers.DefaultRouter()
router.register(r'pings', PingerViewSet)
