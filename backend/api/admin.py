# api/admin.py

from django.contrib import admin
from .models import Estudiante, Profesor  # Importar ambos modelos

admin.site.register(Estudiante)  # Registrar Estudiante
admin.site.register(Profesor)  # Registrar Profesor
