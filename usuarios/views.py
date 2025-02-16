"""Vista de Votos"""
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from eleccion.models import Urna

# Create your views here.

def user_login(request):
    """Login user"""
    print(request.method)
    context = {}
    if request.method=="POST":
        user_name = request.POST.get("user")
        password = request.POST.get("pass")
        user = authenticate(username=user_name, password=password)
        logout(request)
        if user:   #Crear Session
            if not Urna.objects.filter(persona__user_id=user.id).exists():
                login(request, user)
                return redirect('eleccion')#render(request, 'eleccion/voto.html', context)
            else:
                context["error"] = "USTED YA EJERCIO SU DERECHO AL VOTO" 
        else:
            context["error"] = "User or Password incorrect"
            messages.error(request,"Usuario o Contraseña Incorrecta")
    return render(request,'usuarios/login.html', context)


def user_logout(request):
    """Logout USER"""
    logout(request)
    return redirect('user_login')
