from django.db import models
from django.contrib.auth.models import User
from institucion.models import BaseModel, Periodo
# Create your models here.


class Persona(BaseModel):
    identificacion =models.CharField(max_length=10,unique=True)
    nombres  = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.identificacion} {self.nombres} {self.apellidos}'

class Lista(BaseModel):
    nombre = models.CharField(max_length=60)
    logo = models.ImageField(upload_to="img/listas", blank=True, null=True)
    lema = models.TextField(blank=True)
    
    
class Candidato(BaseModel):
    imagen = models.ImageField(upload_to="img/candidatos")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)