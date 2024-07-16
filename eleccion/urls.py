from django.urls import path
from .views import eleccion

urlpatterns = [
    path('', eleccion,name='eleccion'),
]