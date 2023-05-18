
if __name__ == "__main__":
    import os
    import sys
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    from pinger.pinger_api import Pinger
    pinger = Pinger()
    pinger.run_pinger_api()
    print("Stored HOW01-GEN.")
