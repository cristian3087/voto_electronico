"Listado de URL"
from django.urls import path
from .views import eleccion, resultados

urlpatterns = [
    path('', eleccion,name='eleccion'),
    path('resultados/', resultados, name='resultados'),
]