from django.views import View
from django.http import HttpResponse, request
from django.shortcuts import render,redirect
from .forms import FormularioEntregable
from .models import Proyecto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as dj_login , logout
from django.contrib import messages


# Create your views here.

class crear(View):
    template = "crear.html"
    context = {"form": FormularioEntregable}

    def get(self, request):
        
        return render(request, self.template, self.context)

    def post(self, request):
        form=FormularioEntregable(request.POST)
        if form.is_valid():

            proyect=Proyecto()

            proyect.titulo=form.cleaned_data["titulo"]
            proyect.foto=form.cleaned_data["foto"]
            proyect.descripcion=form.cleaned_data["descripcion"]
            proyect.tag=form.cleaned_data["tag"]
            proyect.url=form.cleaned_data["url"]
         
            proyect.save()

            return redirect("proyect:portafolio2")
        
        return HttpResponse("no valido")
    

def portafolio(request):
        proyectos_registrados=Proyecto.objects.all()

        return render(request, "portafolio.html", {"registros":proyectos_registrados})
        pass



class registro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro.html", {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            dj_login(request,usuario)
            return redirect("proyect:crear")

        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])

            return render(request, "registro.html", {"form":form})

    



def login(request):

    if request.method == "POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                dj_login(request, usuario)
                return redirect("crear/")
            else:
                messages.error(request, "usuario no válido")

        else:
            messages.error(request, "información incorrecta")

        #return redirect("crear/")


    form=AuthenticationForm()
    return render(request, "login.html", {"form":form})

def cerrar_sesion(request):
    logout(request)

    return redirect("proyect:login")



def portafolio_general(request):
    return render(request, "portafolio_general.html",{})
