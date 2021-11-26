from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tessiu

# Create your views here.
def home(request):
    L=Tessiu.objects.get_queryset() #Consulta a la base de datos
    template_name="home/index.html"

    listaprocesada=procesaLista()
    
    diccionario={'lista':L,'listaproc':listaprocesada}

    #return render(request,template_name,diccionario)
    return render(request,template_name,{'lista':L})
    #return HttpResponse("Bienvenido Home")

def procesaLista():
    lista1=[]
    a=Tessiu.objects.values('temperatura','color','inflamation')
    #print(a)
    