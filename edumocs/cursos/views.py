from django.shortcuts import render
from .models import Cursos

# Create your views here.
def cursosPrincipal (request):
    cursos = Cursos.objects.all()
    return render (request,'cursos/cursosPrincipal.html',{'cursos':cursos})

