from django.contrib import admin
from .models import Periodo, Entidad
# Register your models here.

admin.site.register([Periodo, Entidad])