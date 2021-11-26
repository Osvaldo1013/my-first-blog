from django.urls import path
from django.urls.resolvers import URLPattern
from .views import grafo,procesaGrafo


urlpatterns = [
    path('grafo/',grafo,name='grafo'),
    path('procesaGrafo',procesaGrafo,name='procesaGrafo')
    
]