import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'message': 'You are connected!'
        }))
