from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def hellworld(request):
    return render(request,"signup.html",{
        'form':UserCreationForm()
    })

def signup(request):
    if request.method=="GET":
        return render(request,"signup.html",{
        'form':UserCreationForm()
        })
    else:
        if request.POST["password1"]== request.POST["password2"]:
            try:
                user=User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                user.save()
                return HttpResponse("Se ha creado el usario exitosamente!")
            except:
                return HttpResponse("Ese nombre de usario ya existe!")
        else:

            return HttpResponse("Las contraseñas no coinciden")