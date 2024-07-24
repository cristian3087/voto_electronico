"""Módulo de Elecciones"""
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Persona
from institucion.models import Periodo
from .models import Candidato, Lista, Urna

# Create your views here.

def resultados(request):
    context ={}
    context['resultados'] = Urna.objects.all()
    context['listas']= listas = Lista.objects.all()
    lst = list(Lista.objects.all().values('nombre'))
    votos = [l.votos for l in listas]
    votos.append(listas.first().votos_nulos)
    votos.append(listas.first().votos_blancos)
    context['lst'] = lst
    context['votos'] = resultados
    
    return render(request, 'eleccion/resultados.html', context)
    

@login_required(login_url='user_login')
def eleccion(request):
    """Vista para elegir un candidato"""
    context = {}
    user = request.user
    print(request)
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('action') == 'guardar_voto':
            persona_id = request.POST.get('persona')
            lista_id = request.POST.get('lista') 
            if lista_id == 'nulo':
                urna= Urna(persona_id=persona_id, tipo = 'NULO')
            elif lista_id == 'blanco': 
                urna= Urna(persona_id=persona_id, tipo = 'BLANCO')
            else:
                urna = Urna(persona_id=persona_id, lista_id=lista_id, tipo='VOTO')
            print(urna)
            urna.save()
            return redirect('user_logout')   
    else:
        if 'u' in request.GET and 'c' in request.GET:
            print(request.GET['u'], request.GET['c'])
            return redirect('user_login')
        
        periodo = Periodo.objects.first()
        context['persona'] =  Persona.objects.get(user_id=user.id)
        #context['candidatos'] = Candidato.objects.all()
        context['periodo'] = Periodo.objects.all().order_by('id').first()
        context['listas'] = Lista.objects.filter(periodo=periodo)
        context['listas_bn'] = [
            {'voto':'BLANCO', 'img': '/static/images/votos/blanco.png'},
            {'voto':'NULO', 'img': '/static/images/votos/nulo1.png'},
            ]
        return render(request, 'eleccion/voto.html', context)