from django.db import models
from institucion.models import BaseModel,Periodo
from usuarios.models import Persona, Candidato
# Create your models here.

class voto(BaseModel):
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    candidato=models.ForeignKey(Candidato, on_delete=models.CASCADE)
    periodo=models.ForeignKey(Periodo, on_delete=models.CASCADE)