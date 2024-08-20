from .models import Pregunta, Respuesta
from .forms import PreguntaForm, RespuestaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pregunta, Respuesta
from .forms import RespuestaForm
from django.contrib.auth.decorators import login_required

def foro_view(request):
    preguntas = Pregunta.objects.filter(es_predefinida= True).order_by('-fecha_pregunta')
    
    context = {
        'preguntas': preguntas,
    }
    return render(request, 'foro/foro.html', context)

@login_required 
def responder_pregunta( request, pregunta_id):
    pregunta = get_object_or_404(Pregunta,id = pregunta_id)

    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit= False)
            respuesta.pregunta = pregunta
            respuesta.respondida_por = request.user
            respuesta.save()

            pregunta.respondida = True
            pregunta.es_predefinida = True
            pregunta.save()

            return redirect('foro_view')
    else:
        form = RespuestaForm()
        return render(request, 'foro/responder.html',{'pregunta':pregunta,'form':form})
