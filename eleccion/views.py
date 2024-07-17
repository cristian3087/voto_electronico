"""Módulo de Elecciones"""
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Persona
from institucion.models import Periodo
from .models import Candidato, Lista

# Create your views here.

@login_required
def eleccion(request):
    """Vista para elegir un candidato"""
    context = {}
    user = request.user
    if 'u' in request.GET and 'c' in request.GET:
        print(request.GET['u'], request.GET['c'])
        return redirect('user_login')
        
    context['persona'] =  Persona.objects.get(id=user.id)
    context['candidatos'] = Candidato.objects.all()
    context['periodo'] = Periodo.objects.all().order_by('id').first()
    context['listas'] = Lista.objects.filter(periodo)
    return render(request, 'eleccion/voto.html', context)