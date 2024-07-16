"""Vista de Votos"""
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
@login_required
def user_login(request):
    """Login user"""
    print(request.method)
    context={}
    if request.method=="POST":
        user_name = request.POST.get("user")
        password = request.POST.get("pass")
        user = authenticate(user_name=user_name, password=password)
        if user:   #Crear Session
            login(request, user)
            return redirect('eleccion')#render(request, 'eleccion/voto.html', context)
        messages.error(request,"Invalid")
        return redirect('user_login')
    return render(request,'usuarios/login.html', context)


def user_logout(request):
    """Logout USER"""
    logout(request)
    return redirect('user_login')