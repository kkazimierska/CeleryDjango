from rest_framework import serializers
from pinger.models import Pings

class PingerSerializer(serializers.Serializer):

    class Meta:
        model = Pings
        fields = '__all__'
