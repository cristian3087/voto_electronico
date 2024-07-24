from django.contrib import admin
from eleccion.models import Cargo, Lista, Candidato, Urna

admin.site.register([Cargo, Lista, Candidato, Urna])