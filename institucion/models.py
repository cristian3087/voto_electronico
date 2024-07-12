from django.db import models
from common.models import BaseModel
    
class Periodo(BaseModel):
    nombre = models.CharField(max_length=80)
    inicio = models.DateField(verbose_name='Fecha inicio')
    fin = models.DateField(verbose_name='Fecha fin')
    activo = models.BooleanField(default=False)
    def __str__(self) -> str:
        estado = '✔️' if self.activo else '❌'

        return f'{self.nombre} ({self.inicio}-{self.fin}) {estado}'
    
class Entidad(BaseModel):
    nombre = models.CharField(max_length=60)
    foto = models.ImageField(upload_to='img/entidad', null=True, blank=True)
    direccion = models.CharField(max_length=100, blank=True, default='')
    def __str__(self) -> str:
        return f'{self.nombre}, {self.direccion}'
    