from django.db import models
from django.contrib.auth.models import User
from institucion.models import BaseModel
# Create your models here.


class Persona(BaseModel):
    identificacion =models.CharField(max_length=10,unique=True)
    nombres  = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    habilitado =models.BooleanField(default=True)
    
    @property
    def nombres_completos(self):
        "Nombres completos"
        return f"{self.nombres} {self.apellidos}"
    
    def __str__(self) -> str:
        return f'{self.identificacion} {self.nombres} {self.apellidos}'