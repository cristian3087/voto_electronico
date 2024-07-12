from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.
# Create your models here.
class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, related_name="%(class)s_creado_por", on_delete=models.SET_NULL, null=True)
    usuario_modificacion = models.ForeignKey(User, related_name="%(class)s_modificado_por", on_delete=models.SET_NULL, null=True)
    
    class Meta:
        abstract = True