from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from cursos.models import Cursos
from .forms import cursosForm
from .forms import PruebaForm
from .models import Prueba
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def panelPrincipal(request):
    curso = Cursos.objects.all()
    return render(request,'administrador/administrador.html',{'cursos':curso})

@login_required
def listaUsuarios(request):
    # Obtener el usuario que ha iniciado sesión
    usuario = request.user
    # Obtener los detalles del usuario
    usuario_detalles = {
        'nombre': usuario.get_full_name(),
        'correo_electronico': usuario.email,
        'numero_telefono': usuario.profile.telefono if hasattr(usuario, 'profile') else '',
        'fecha_nacimiento': usuario.profile.fecha_nacimiento if hasattr(usuario, 'profile') else '',
        'nombre_usuario': usuario.username,
        'genero': usuario.profile.genero if hasattr(usuario, 'profile') else ''
    }
    return render(request, 'administrador/administrador.html', {'usuario_detalles': usuario_detalles})

def eliminarCurso(request,id,confirmacion='administrador/confirmarEliminacion.html'):
    cursos = get_object_or_404(Cursos,id=id)
    if request.method=='POST':
        cursos.delete()
        curso=Cursos.objects.all()
        return render(request,"administrador/administrador.html",{'cursos':curso})

    return render(request, confirmacion, {'object':cursos})


def altaCurso(request):
    if request.method == 'POST':
        form = cursosForm(request.POST,request.FILES)
        if form.is_valid(): 
            nombre = request.POST['nombre']
            costo = request.POST['costo']
            fecha_ini = request.POST['fecha_inicio']
            fecha_term = request.POST['fecha_termino']
            horas = request.POST['horas']
            cupos = request.POST['cupos']
            imagen = request.FILES['imagen']
            descripcion = request.POST['descripcion']
            insert = Cursos(nombre = nombre,costo = costo, fecha_inicio=fecha_ini, fecha_termino=fecha_term,
                            horas=horas,cupos=cupos,imagen=imagen,descripcion=descripcion)
            insert.save()
            cursos=Cursos.objects.all()
            return render(request,"administrador/continuar.html",{'curso':cursos})
    form = cursosForm()
    return render(request,'administrador/altaCursos.html',{'form':form})

def continuar(request):
    return render(request,'administrador/continuar.html')

class CustomLoginView(auth_views.LoginView):
    template_name = 'administrador/custom_login.html'

    def form_valid(self, form):
        user = form.get_user()
        
        # Verifica si el usuario pertenece al grupo "Administradores"
        if user.groups.filter(name='Administradores').exists():
            return render(self.request, 'administrador/administrador.html')  # Redirige al panel de administrador
        else:
            return render(self.request, 'contenido/inicio.html')  # Redirige a la página de inicio para otros usuarios

##################################Editar Cursos, aún en pruebas no tocar###################################################################
def consultarCursoIndividual(request, id):
    curso=Cursos.objects.get(id=id)
    return render(request,"administrador/editarCurso.html",{'curso':curso})


def editarCurso(request, id):
        
        curso = get_object_or_404(Cursos, id=id) 
        form = cursosForm(request.POST,instance=curso)
        if form.is_valid(): 
            
            form.save()
            cursos = Cursos.objects.all()
            return render(request,"administrador/administrador.html",{'cursos':cursos})

        return render(request,"administrador/editarCurso.html",{'curso':curso})

def prueba(request):
    if request.method == 'POST':
        form = PruebaForm(request.POST)
        if form.is_valid(): 
            form.save()
            cursos=Prueba.objects.all()
            return render(request,"administrador/administrador.html",{'curso':cursos})
    form = cursosForm()
    return render(request,'administrador/altaCursos.html',{'form':form})