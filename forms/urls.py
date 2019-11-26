from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path(r'checkIn', views.checkIn),
    path(r'checkOut', views.checkOut)
]