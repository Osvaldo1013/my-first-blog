from django.urls import path
from django.urls.resolvers import URLPattern
from .views import about
app_name = 'about'

urlpatterns = [
    path('about/',about,name='about')
]