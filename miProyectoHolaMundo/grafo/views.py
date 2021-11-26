from django.http.response import HttpResponse
from django.shortcuts import render
from scipy.spatial import distance
from home.models import Tessiu
# Create your views here.

def grafo(request):
    template_name = "grafo/grafo.html"
    
    return render(request,template_name)
def procesaGrafo(request):
    template_name = "grafo/grafo.html"
    umbral=0
    if request.method  == 'GET':
        umbral=float(request.GET.get('umbral'))
    L = Tessiu.objects.get_queryset()
    listaprocesada = distancia(L,umbral)
    diccionario = {'listap':listaprocesada}
    return render(request, template_name, diccionario)

def distancia(datos,a):
    final = []
    dist = []
    tabla1 = []
    for i in datos:
        dato = []
        dato.append(i.temperatura),dato.append(i.color),dato.append(i.inflamation)
        final.append(dato)      
    
    for i in range(len(final)):
        aux = []
        for j in range(len(final)):
            aux.append(distance.euclidean(final[i],final[j],10))
        dist.append(aux)
   
    for i in range(len(dist)):
        for j in range(i,len(dist)):
            v0 = i
            vf = j
            mag = dist[i][j]
            if  mag <= a:
             tabla1.append((v0,vf,mag,"Si"))
            elif mag >= a:
             tabla1.append((v0,vf,mag,"No"))
    return tabla1
