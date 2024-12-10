from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profesor,Estudiante

class FormularioP(UserCreationForm):
    foto=forms.ImageField(required=True)
    direccion=forms.CharField(max_length=255,required=True)

    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2']

    def save(self,commit=True):
        user=super(FormularioP,self).save(commit=False)
        if commit:
            user.save()
            Profesor.objects.create(
                user=user,
                foto=self.cleaned_data['foto'],
                direccion=self.cleaned_data['direccion'],
                rol="profesor"
            )
        return user
    
class FormularioE(UserCreationForm):

    username=forms.CharField(max_length=150,required=True)
    registro=forms.ImageField(required=True)
    carrera=forms.CharField(max_length=255,required=True)
    codigoE=forms.IntegerField(required=True)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def save(self,commit=True):
        user=super(FormularioE,self).save(commit=False)
        if not user.username:
            user.username=self.cleaned_data['email']
        if commit:
            user.save()
            Estudiante.objects.create(
                user=user,
                registro=self.cleaned_data['registro'],
                carrera=self.cleaned_data['carrera'],
                codigoE=self.cleaned_data['codigoE'],
                rol="estudiante"
            )
        return user
    
    
class FormularioLoginP(forms.Form):
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingresa tu correo"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingresa tu contraseña"})
    )
