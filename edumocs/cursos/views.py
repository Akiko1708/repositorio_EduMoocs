
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
            cupos_restantes = curso.cupos - 1
            curso.cupos_restantes +=1 
            curso.cupos = cupos_restantes
            curso.save()
            preinscripcion.save()
            return redirect('confirmacion')
        else:
            return render(request, 'cursos/no_cupos.html')
    else:
        form = PreinscripcionesForm()
    return render (request,'cursos/preinscripcion.html',{'form':form,'curso':curso})

def confirmacion(request):
    return render(request,'cursos/confirmacion.html')

def no_cupos(request):
    return render (request,'cursos/no_cupos.html')

