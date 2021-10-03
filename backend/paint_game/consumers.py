import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from accounts.models import Accounts
from .models import Room, UserInRoom, Paint
from accounts.models import Accounts
# from accounts.serializers import AccountsSerializer
from channels.db import database_sync_to_async

def get_users():
    ''' (확실하진 않으나) evaluate를 위해서.. 
        list(~~~)
        이 작업이 없으면 async함수 안에서 users = await database_sync_to_async(get_users)() 로 
        users를 쓸 수 없음 
        ex) print(users) 여기서 에러 발생
    '''        
    users = list(Accounts.objects.all())
    # serializer = AccountsSerializer(users, many=True)
    return users

def create_user():
    now = datetime.datetime.now()
    print(now)
    return Accounts.objects.create(user_name="kim", time_to_expire=now)

def game_start(room_num):
    room = Room.objects.get(room_id = room_num)
    # 방에 들어있던 점수들 모두 삭제
    room.score_set.all().delete()
    room.is_started = True
    room.save()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = 'game_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("socket created")
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("text_data:", text_data_json)
        flag = text_data_json['type']
        if flag == 'chat':
            # Send message to room group
            await self.group_send('send_message', message)
        elif flag == 'game':
            await database_sync_to_async(game_start)(self.room_name)
            await self.group_send('send_message', 'game started')

    # Receive message from room group
    async def send_message(self, event):
        print("event:", event)
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    def group_send(self, type, message):
        return self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type,
                'message': message
            }
        )
# class GameConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'game_%s' % self.room_name
#
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#     # Receive message from WebSocket
#     async def receive(self):
#         # await database_sync_to_async(create_user)()
#
#         room = Room.objects.get()
#         room.is_started = True
#         room.save()
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'start_messsage',
#                 'message': "game_started"
#             }
#         )
#
#     # Receive message from room group
#     async def start_message(self, event):
#         message = event['message']
#         print(event)
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))