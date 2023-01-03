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
        form=FormularioEntregable(request.POST or None, request.FILES or None)
       
        if form.is_valid():
            
            proyect=Proyecto()
            
            proyect.titulo=form.cleaned_data["titulo"]
            proyect.foto=form.cleaned_data["foto"]
            proyect.descripcion=form.cleaned_data["descripcion"]
            proyect.tag=form.cleaned_data["tag"]
            proyect.url=form.cleaned_data["url"]
            print(proyect.foto)
            proyect.save()

            return redirect("proyect:portafolio2")
        
        return HttpResponse("no valido")
    

def portafolio(request):
        proyectos_registrados=Proyecto.objects.all()

        return render(request, "portafolio.html", {"registros":proyectos_registrados})
  
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

    proyectos_registrados=Proyecto.objects.all()
    return render(request, "portafolio_general.html", {"registros":proyectos_registrados})
    


def delete(request, id):

    form_filter=Proyecto.objects.filter(id=id)
    form_filter.delete()
    return redirect("proyect:portafolio2")

class edit(View):
 
    def get(self, request, id):
        form_filter=Proyecto.objects.filter(id=id)[0]

        return render(request, "edit.html", {"proyecto":form_filter})

    def post(self, request, id):
        
        titulo=request.POST["titulo"]
        tag=request.POST["tag"]
        descripcion=request.POST["descripcion"]
        url=request.POST["url"]
        #foto=request.POST["foto"]  #si quito el enctype y pongo foto=request.POST["foto"] entonces cuando yo ponga en el html : <td>{{item.foto.url}}</td>  esto me da /media/foto.jpg -> es decir to me da lo correcto que sería -> /media/images/foto.jpg
        foto=request.FILES["foto"]  #el enctype hace que yo pueda subir de forma correcta a mi bbdd para que después pueda ser leído y mostrar la foto

        proyect=Proyecto.objects.filter(id=id)[0]
        
        proyect.titulo=titulo
        proyect.foto=foto      #si lees la línea 124 y piensas ponerle proyect.foto="images/"+ request.POST["foto"] entonces pensarías que funcionaría pero no es así. por eso vuelve a leer la línea 125
        proyect.descripcion=descripcion         
        proyect.tag=tag     
        proyect.url=url
        print(proyect.foto)
        proyect.save()

    

        return redirect("proyect:portafolio2")





       
        