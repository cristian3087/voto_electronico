from django.db import models

# Create your models here.
class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
class Periodo(BaseModel):
    nombre = models.CharField(max_length=80)
    inicio = models.DateField(verbose_name=u'Fecha inicio')
    fin = models.DateField(verbose_name=u'Fecha fin')
    activo = models.BooleanField(default=False)
    
class Entidad(BaseModel):
    nombre = models.CharField(max_length=60)
    foto = models.ImageField(upload_to='img/entidad')
    direccion = models.CharField(max_length=100)
    