from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta
from .forms import PreguntaForm, RespuestaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pregunta, Respuesta
from .forms import RespuestaForm

def foro_view(request):
    preguntas = Pregunta.objects.all().order_by('-fecha_pregunta')
    if request.method == 'POST':
        pregunta_form = PreguntaForm(request.POST)
        if pregunta_form.is_valid():
            pregunta_form.save()
            return render(request,'foro/foro.html')
    else:
        pregunta_form = PreguntaForm()
    
    context = {
        'preguntas': preguntas,
        'pregunta_form': pregunta_form
    }
    return render(request, 'foro/foro.html', context)

def responder_view(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    if request.method == 'POST':
        respuesta_form = RespuestaForm(request.POST)
        if respuesta_form.is_valid():
            respuesta = respuesta_form.save(commit=False)
            respuesta.pregunta = pregunta
            respuesta.save()
            return render(request,'foro/foro.html')
    else:
        respuesta_form = RespuestaForm()
    
    context = {
        'pregunta': pregunta,
        'respuesta_form': respuesta_form
    }
    return render(request, 'foro/responder.html', context)



def responder_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    
    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.pregunta = pregunta
            respuesta.save()
            return redirect('listar_preguntas')  # Redirigir a la lista de preguntas
    else:
        form = RespuestaForm()

    return render(request, 'responder.html', {'pregunta': pregunta, 'form': form})
