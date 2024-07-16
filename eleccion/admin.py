from django.contrib import admin
from eleccion.models import Cargo, Lista, Candidato

admin.site.register([Cargo, Lista, Candidato])

