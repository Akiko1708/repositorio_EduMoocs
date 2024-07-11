from django.contrib import admin
from .models import Cursos


class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('id','nombre','profesor')
    search_fields =('id','nombre','profesor')
    date_hierarchy = 'created'
    list_filter = ('profesor','fecha_inicio','fecha_termino')

admin.site.register(Cursos,AdministrarCurso)
