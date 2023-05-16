from django.db import models

class PingStatus(models.TextChoices):
    ONLINE = 'Online'
    OFFLINE = 'Offline',
    UNKNOWN = 'Unknown'

class PingerManager(models.Manager):
    pass

# Create your models here.
class Pings(models.Model):
    windfarm_name: models.CharField(max_length=20)
    turbine_host: models.GenericIPAddressField()
    status = models.CharField(
        max_length=8,
        choices=PingStatus.choices,
        default=PingStatus.UNKNOWN,
        null=False
    )
    host = models.GenericIPAddressField(null=False)

    class Meta:
        db_table='pings'

    objects = PingerManager()

    @staticmethod
    def store_results():
        pass
