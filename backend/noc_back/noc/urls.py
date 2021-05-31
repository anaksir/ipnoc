from django.urls import path
from . import views


urlpatterns = [
    path('time/', views.current_datetime),
    path('devices/', views.DeviceList.as_view()),
]
