# api/serializers.py

from rest_framework import serializers
from .models import Estudiante, Profesor

# Serializador para Estudiantes
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'correoInstitucional', 'numeroCelular', 'codigoEstudiante']

# Serializador para Profesores
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['documento', 'direccion', 'email', 'password', 'photo']
