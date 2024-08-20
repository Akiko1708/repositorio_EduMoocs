from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_pregunta = models.DateTimeField(auto_now_add=True)
    es_predefinida = models.BooleanField(default=False)
    respondida = models.BooleanField(default= False)
    notificado = models.BooleanField(default= False)

    def __str__(self):
        return f"Pregunta :{self.mensaje} - Predefinida: {'Si'if self.es_predefinida  else'No'}"

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    respuesta = models.TextField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    respondida_por = models.ForeignKey(User, on_delete=models.SET_NULL,null= True, blank= True)

    def __str__(self):
        return f"Respuesta a la pregunta: {self.pregunta.mensaje}"
    


