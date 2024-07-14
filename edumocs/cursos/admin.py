from django.contrib import admin
from .models import Cursos


class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('id','nombre','profesor','fecha_inicio','fecha_termino','horas','cupos','imagen')
    search_fields =('id','nombre','profesor')
    date_hierarchy = 'created'
    list_filter = ('profesor','fecha_inicio','fecha_termino')
    list_display_links=('horas','nombre','profesor')
    list_per_page=5
    list_editable=('cupos',)
    class Media:
        css = {
            'all': ('edumocs/css/custom_admin.css',)
            }
admin.site.register(Cursos,AdministrarCurso)
