from django.contrib import admin
from .models import Paciente, Tessiu

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    

    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)
   
    
class TessiuAdmin(admin.ModelAdmin):
    list_display = ('color','temperatura','inflamation','name')    
    search_fields = ('color',)
    list_filter = ('color','name',)

admin.site.register(Tessiu, TessiuAdmin)
