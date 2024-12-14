from django.db import models

class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoInstitucional = models.EmailField(unique=True)
    numeroCelular = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Para almacenar la contraseña
    codigoEstudiante = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombres


class Profesor(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.email
