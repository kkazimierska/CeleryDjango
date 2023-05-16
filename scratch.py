from pinger.models import Pings, PingStatus

pings = Pings(windfarm_name='Walny 2', turbine_name = 'X01-W23', host='100.123.45.3', status=PingStatus.ONLINE)
pings.save()