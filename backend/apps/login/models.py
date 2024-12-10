from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profesor', null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    rol= models.CharField(max_length=50, default="profesor",editable=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Estudiante(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    codigoE = models.IntegerField()
    carrera= models.CharField(max_length=25)
    registro= models.ImageField(upload_to='estudiante', null=False, blank=False)
    rol= models.CharField(max_length=50, default="estudiante",editable=False)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
