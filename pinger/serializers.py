from rest_framework import serializers
from pinger.models import Pings

class PingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pings
        fields = '__all__'
