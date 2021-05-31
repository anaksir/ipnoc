from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
import datetime
from .models import Device


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def dev_list(request):
    devices = Device.objects.all()
    return render(request, 'noc/device_list.html', {'devices': devices})


class DeviceList(ListView):
    queryset = Device.objects.all()
    context_object_name = 'devices'
    template_name = 'noc/device_list.html'
