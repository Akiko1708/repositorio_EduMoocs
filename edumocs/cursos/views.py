from django.shortcuts import render
from .models import Cursos

# Create your views here.
def cursosPrincipal (request):
    curso = Cursos.objects.all()
    return render (request,'cursos/cursosPrincipal.html',{'cursos':curso})

def cursoContenido (request,id):
    curso = Cursos.objects.get(id=id)
    return render (request,'cursos/cursoContenido.html',{'cursos':curso})

def preinscripcion (request):
    return render (request,'cursos/preinscripcion.html')

