from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Pregunta, Respuesta

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        mensaje = data['message']
        es_predefinida = data['es_predefinida']

        pregunta = Pregunta.objects.create(texto=mensaje, es_predefinida=es_predefinida)

        if es_predefinida:
            respuesta_texto = buscar_respuesta_automatica(mensaje)
            Respuesta.objects.create(pregunta=pregunta, texto=respuesta_texto)
            await self.send(text_data=json.dumps({'message': f"Q: {mensaje}\nA: {respuesta_texto}"}))
        else:
            await self.send(text_data=json.dumps({'message': f"Usuario: {mensaje}\nUn administrador responderá pronto."}))

def buscar_respuesta_automatica(pregunta):
    respuestas = {
        "¿Cómo resetear mi contraseña?": "Para resetear tu contraseña, sigue estos pasos...",
        "¿Cómo actualizar mi perfil?": "Puedes actualizar tu perfil accediendo a la sección de configuración..."
    }
    return respuestas.get(pregunta, "Lo siento, no tengo una respuesta para eso.")
