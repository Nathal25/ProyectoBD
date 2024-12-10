from django.shortcuts import render,redirect
from .forms import FormularioP,FormularioLoginP,FormularioE
from django.contrib.auth.hashers import check_password
from .models import Profesor,Estudiante

# Create your views here.



def login(request):
    if request.method == 'POST':
        # Procesar el formulario
        form = FormularioLoginP(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Buscar el profesor o estudiante por correo
                user = None
                try:
                    profesor = Profesor.objects.get(user__email=email)
                    user = profesor
                except Profesor.DoesNotExist:
                    estudiante = Estudiante.objects.get(user__email=email)
                    user = estudiante

                # Validar la contraseña
                if check_password(password, user.user.password):
                    # Guardar información en la sesión
                    if user.rol == "profesor":
                        request.session['profesor_id'] = user.id
                        return redirect('CursosP')
                    elif user.rol == "estudiante":
                        request.session['estudiante_id'] = user.id
                        return redirect('CursosE')
                else:
                    return render(request, 'login/login.html', {'form': form, 'error': 'Contraseña incorrecta'})
            except (Profesor.DoesNotExist, Estudiante.DoesNotExist):
                return render(request, 'login/login.html', {'form': form, 'error': 'Correo no registrado'})
    else:
        form = FormularioLoginP()

    return render(request, 'login/login.html', {'form': form})



def registroP(request):
    if request.method == 'POST':
        form=FormularioP(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioP()
    return render(request,"login/registroP.html",{'form':form})

def registroE(request):
    if request.method == 'POST':
        form=FormularioE(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioE()
    return render(request,"login/registroE.html",{'form':form})
