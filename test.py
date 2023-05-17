
if __name__ == "__main__":
    from pinger.pinger_api import Pinger
    pinger = Pinger()
    pinger.run_pinger_api()
    import os
    import sys
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

    from pinger.models import Pings, PingStatus

    pings = Pings.objects.create(host='100.123.45.3', status=PingStatus.ONLINE)
    pings.save()
    print("Stored Walny 2")