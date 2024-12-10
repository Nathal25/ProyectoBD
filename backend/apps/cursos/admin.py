from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'get_profesor')
    
    def get_profesor(self, obj):
        return f"{obj.profesor.first_name} {obj.profesor.last_name}"
    get_profesor.short_description = 'Profesor'