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
        es_predefinida = data.get('es_predefinida', False)

        pregunta, created = Pregunta.objects.get_or_create(mensaje=mensaje, defaults={'es_predefinida': es_predefinida})
        
        if pregunta.es_predefinida:
            respuesta = Respuesta.objects.filter(pregunta=pregunta).first()
            if respuesta:
                await self.send(text_data=json.dumps({
                    'message': f"Q: {mensaje}\nA: {respuesta.respuesta}"
                }))
        else:
            await self.send(text_data=json.dumps({
                'message': f"Usuario: {mensaje}\nUn administrador responderá pronto."
            }))
