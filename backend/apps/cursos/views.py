from django.shortcuts import render,redirect
from .models import Curso
from login.models import Profesor
# Create your views here.

# Create your views here.
def cursosP(request):
    if 'profesor_id' not in request.session:
        return redirect('login')
    profesor_id=request.session['profesor_id']
    try: 
        profesor=Profesor.objects.get(id=profesor_id)
        cursos=Curso.objects.filter(profesor=profesor.user)
        return render(request,"cursos/cursosP.html",{'cursosP':cursosP})
    except Profesor.DoesNotExist:
        del request.session['profesor_id']
        return redirect('login')
    

def crearCurso(request):
    if 'profesor_id' not in request.session:
        return redirect('login')
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        profesor_id=request.session['profesor_id']
        try:
            profesor=Profesor.objects.get(id=profesor_id)
            if nombre:
                Curso.objects.create(
                    nombre=nombre,
                    profesor=profesor.user
                )
                return redirect('Cursos')
            else:
                return render(request,'cursos/crearCurso.html',{'error':'Debe ingresar un nombrer para el curso'})
        except Profesor.DoesNotExist:
            return redirect('login')
    return render(request, 'cursos/crearCurso.html')

def cursosE(request):
    return render(request,'cursos/cursosE.html')

