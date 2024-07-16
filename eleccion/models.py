from django.db import models
from institucion.models import BaseModel,Periodo
from usuarios.models import Persona
from common.models import BaseModel
# Create your models here.

class Cargo(BaseModel):
    nombre = models.CharField(max_length=60)
    alias = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.nombre}'
    
    
class Lista(BaseModel):
    nombre = models.CharField(max_length=60)
    logo = models.ImageField(upload_to="img/listas", blank=True, null=True)
    lema = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'({self.pk}) {self.nombre} {self.lema}'
    
    
class Candidato(BaseModel):
    imagen = models.ImageField(upload_to="img/candidatos")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'({self.pk}: {self.persona},  {self.cargo})({self.lista})'


class voto(BaseModel):
    TIPOS_VOTO = [
        ('Candidato', 'Candidato'),
        ('Blanco', 'Blanco'),
        ('Nulo', 'Nulo')
    ]
    persona  = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='votos')
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True, blank=True, related_name='votos')
    

    
    
    
