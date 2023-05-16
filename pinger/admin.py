from django.contrib import admin

# Register your models here.
from pinger.models import Pings

class PingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pings, PingAdmin)
