from django.urls import path
from django.urls.resolvers import URLPattern
from .views import sintactico


urlpatterns = [
    path('sintactico/',sintactico,name='sintactico')

]