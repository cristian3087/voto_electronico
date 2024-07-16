from django.shortcuts import render

# Create your views here.
def eleccion(request):
    context = {}
    context['user'] = user = request.user
    return render(request, 'eleccion/voto.html', context)