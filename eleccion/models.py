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
    
class Candidato(BaseModel):
    imagen = models.ImageField(upload_to="img/candidatos")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    #lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'({self.pk}: {self.persona},  {self.cargo})'

    
class Lista(BaseModel):
    nombre = models.CharField(max_length=60)
    logo = models.ImageField(upload_to="img/listas", blank=True, null=True)
    lema = models.TextField(blank=True, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    candidato = models.ManyToManyField(Candidato)
    def __str__(self):
        return f'({self.pk}) {self.nombre} {self.lema}'
    
    @property
    def representante(self):
        return self.candidato.all().first()
        
    @property
    def directiva(self):
        return self.candidato.all().exclude(self.representante)
        
    @property
    def votos_nulos(self):
        return Urna.objects.filter(tipo='NULO').count()
    
    @property
    def votos_blancos(self):
        return Urna.objects.filter(tipo='BLANCO').count()
    
    @property
    def votos(self):
        return Urna.objects.filter(lista_id=self.id).count()
    @property
    def votos_totales(self):
        return Urna.objects.all().count()


class Urna(BaseModel):
    persona  = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='votos')
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(default='VOTO', max_length=6)
    
