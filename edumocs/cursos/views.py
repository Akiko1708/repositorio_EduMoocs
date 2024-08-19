
from django.shortcuts import render,redirect
from .models import Cursos
from .forms import PreinscripcionesForm

# Create your views here.
def cursosPrincipal (request):
    curso = Cursos.objects.all()
    return render (request,'cursos/cursosPrincipal.html',{'cursos':curso})

def cursoContenido (request,id):
    curso = Cursos.objects.get(id=id)
    return render (request,'cursos/cursoContenido.html',{'cursos':curso})

def preinscripcion (request,curso_id):
    curso = Cursos.objects.get(id=curso_id)
    if request.method == 'POST':
        form = PreinscripcionesForm(request.POST)
        if form.is_valid():
            preinscripcion = form.save(commit = False)
            preinscripcion.curso = curso 
            preinscripcion.save()
            return redirect('confirmacion')
        else:
            print(form.errors)
    else:
        form = PreinscripcionesForm()
    return render (request,'cursos/preinscripcion.html',{'form':form,'curso':curso})

def confirmacion(request):
    return render(request,'cursos/confirmacion.html')

