from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class Persona(BaseModel):
    identificacion =models.CharField(max_length=10,unique=True)
    nombres  = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.identificacion} {self.nombres} {self.apellidos}'
    