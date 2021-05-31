from django.contrib import admin
from .models import Device, Region, Order, Client, Interface


admin.site.register(Region)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Interface)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip_address', 'region')
