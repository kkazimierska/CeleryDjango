from django.db import models

# Create your models here.
class Pings(models.Model):
    windfarm_name: models.CharField(max_length=20)
    turbine_host: models.GenericIPAddressField()
