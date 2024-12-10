from django.db import models
from django.conf import settings

class Curso(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del curso
    profesor = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Referencia al usuario que lo crea
        on_delete=models.CASCADE,  # Si se elimina el profesor, se eliminan sus cursos
        related_name="cursos"
    )

    def __str__(self):
        return self.nombre
    

