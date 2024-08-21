from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Pregunta, Respuesta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def foro_view(request):
    preguntas = Pregunta.objects.filter(es_predefinida=True)
    return render(request, 'foro/foro.html', {'preguntas': preguntas})

@login_required
def responder_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    
    if request.method == "POST":
        respuesta = request.POST.get('respuesta')
        Respuesta.objects.create(pregunta=pregunta, respuesta=respuesta, respondida_por=request.user)
        pregunta.respondida = True
        pregunta.es_predefinida = True
        pregunta.save()
        return JsonResponse({'status': 'success'})
    
    return render(request, 'foro/responder.html', {'pregunta': pregunta})

@csrf_exempt
def enviar_pregunta(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje').strip()
        print(f"Mensaje recibido: {mensaje}")  # Depuración

        es_predefinida = Pregunta.objects.filter(mensaje=mensaje, es_predefinida=True).exists()
        print(f"¿Es predefinida?: {es_predefinida}")  # Depuración

        if es_predefinida:
            pregunta = Pregunta.objects.get(mensaje=mensaje, es_predefinida=True)
            respuesta = Respuesta.objects.get(pregunta=pregunta)
            return JsonResponse({'respuesta': respuesta.respuesta})
        else:
            # Aquí se debe notificar a los administradores
            print("Pregunta no predefinida, notificando a administradores")  # Depuración
            return JsonResponse({'respuesta': "Un administrador responderá pronto."})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
