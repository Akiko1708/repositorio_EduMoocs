"""
URL configuration for edumocs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as views_cursos
from administrador import views as viewsAdmin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio ,name="Inicio"),
    path('cursos/',views_cursos.cursosPrincipal,name="Cursos"),
    path('acercade/',views.acercade,name="Acercade"),
    path('preguntas/',views.preguntas,name="Preguntas"),
    path('foro/',views.foro,name="Foro"),
    path('eliminarCursos/<int:id>/',viewsAdmin.eliminarCurso,name='Eliminar'),
    path('administrador/',viewsAdmin.panelPrincipal,name="Administrador"),
    path('cursoEditado/<int:id>/',viewsAdmin.editarCurso,name='Editar'),
    path('editarCurso/<int:id>/',viewsAdmin.consultarCursoIndividual,name='ConsultaIndividual'),
    path('altaCursos/',viewsAdmin.altaCurso,name='Alta'),
    path('continuar/',viewsAdmin.continuar,name='Continuar'),
    path('cursoContenido/',views_cursos.cursoContenido,name = 'CursoContenido'),
    path('preinscripcion/',views_cursos.preinscripcion,name = 'Preinscripcion'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
