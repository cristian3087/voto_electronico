"""Módulo de Elecciones"""
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import Persona
from .models import Candidato
# Create your views here.

@login_required
def eleccion(request):
    """Vista para elegir un candidato"""
    context = {}
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        
        return JsonResponse({'respuesta': 'ok'})
        #return HttpResponse(json.dumps({'result':'OK'}}),content_type='application/json')
    
    context['persona'] =  Persona.objects.get(id=user.id)
    context['candidatos'] = Candidato.objects.all()
    return render(request, 'eleccion/voto.html', context)