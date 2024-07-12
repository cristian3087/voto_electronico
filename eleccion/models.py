from django.db import models
from institucion.models import BaseModel,Periodo
from usuarios.models import Persona, Candidato
from common.models import BaseModel
# Create your models here.

class voto(BaseModel):
    TIPOS_VOTO = [
        ('Candidato', 'Candidato'),
        ('Blanco', 'Blanco'),
        ('Nulo', 'Nulo')
    ]
    persona  = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='votos')
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True, blank=True, related_name='votos')
    
    