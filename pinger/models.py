from django.db import models
from typing_extensions import TypedDict
from django.utils import timezone

class PingStatus(models.TextChoices):
    ONLINE = 'Online'
    OFFLINE = 'Offline',
    UNKNOWN = 'Unknown'

class PingerParse(TypedDict):
    ping_sent: int
    ping_rcv: int
    prc_lost: int
    time_avg: float
    status: str

class PingerManager(models.Manager):
    pass

class Pings(models.Model):
    windfarm_name = models.CharField(default = "HOW01-GEN", max_length=20)
    turbine_name = models.CharField(default = "X01YCA01UH002", max_length=20)
    status = models.CharField(
        max_length=8,
        choices=PingStatus.choices,
        default=PingStatus.UNKNOWN,
        null=False
    )
    host = models.GenericIPAddressField(default='212.77.98.9', null=False)
    last_pinged = models.DateTimeField(verbose_name='Last time the IP was pinged', default=timezone.now)

    class Meta:
        db_table='pings'

    objects = PingerManager()

    @staticmethod
    def store_results():
        pass

