from django.contrib import admin
from .models import Profesor, Estudiante

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id','get_nombre_completo', 'get_email', 'foto','rol')
    
    def get_nombre_completo(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_nombre_completo.short_description = 'Nombre Completo'
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Correo Electrónico'


