from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home
app_name = 'home'

urlpatterns = [
    path('',home,name='home')


]