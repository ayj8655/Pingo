from asyncio.windows_events import NULL
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from accounts.models import Accounts
from channels.db import database_sync_to_async

def get_users():
    users = Accounts.objects.all()
    for user in users:
        print(user.user_name)
    return users

def create_user():
    now = datetime.datetime.now()
    print(now)
    return Accounts.objects.create(user_name="kim", time_to_expire=now)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    async def receive(self, text_data):
        # await database_sync_to_async(create_user)()

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(text_data_json)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))