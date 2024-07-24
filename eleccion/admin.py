from django.contrib import admin
from eleccion.models import Cargo, Lista, Candidato, Urna

class UrnaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'lista', 'tipo')
    order_display = ('persona')

#admin.site.register(Urna, UrnaAdmin)
admin.site.register([Cargo, Lista, Candidato])
admin.site.register(Urna, UrnaAdmin)