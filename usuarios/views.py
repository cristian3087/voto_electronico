from django.shortcuts import render

# Create your views here.

def user_login(request):
    context={}
    print(request.method)
    return render(request,'usuarios/login.html', context)