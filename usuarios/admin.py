# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
from .forms import UploadExcelForm
from django.contrib.auth.models import User
from usuarios.models import Persona, Cargo, Lista, Candidato

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombres', 'apellidos', 'email', 'user')
    search_fields = ('identificacion', 'nombres', 'apellidos', 'email')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-excel/', self.admin_site.admin_view(self.import_excel), name='import_excel'),
        ]
        return custom_urls + urls

    def import_excel(self, request):
        if request.method == "POST":
            form = UploadExcelForm(request.POST, request.FILES)
            if form.is_valid():
                excel_file = request.FILES["excel_file"]
                df = pd.read_excel(excel_file)

                for index, row in df.iterrows():
                    identificacion = str(row['identificacion'])
                    nombres = row['nombres']
                    apellidos = row['apellidos']
                    email = row['email']

                    # Crear usuario
                    user, created = User.objects.get_or_create(username=identificacion, email=email)
                    if created:
                        user.set_password(identificacion)#User.objects.make_random_password())
                        user.first_name = nombres.split(' ')[0]
                        user.last_name = apellidos.split(' ')[0]
                        user.save()

                    # Crear persona
                    Persona.objects.create(
                        identificacion=identificacion,
                        nombres=nombres,
                        apellidos=apellidos,
                        email=email,
                        user=user
                    )

                messages.success(request, "Las personas se han importado con éxito.")
                return redirect("..")
        else:
            form = UploadExcelForm()

        context = {
            "form": form,
        }
        return render(request, "admin/import_excel.html", context)

admin.site.register(Persona, PersonaAdmin)
admin.site.register([Cargo, Lista, Candidato])
