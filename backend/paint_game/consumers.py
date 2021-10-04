import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime

from django.db.models.query_utils import Q
from accounts.models import Accounts
from .models import Room, UserInRoom, Paint
from accounts.models import Accounts
from accounts.serializers import AccountsSerializer
from paint_game.serializers import RoomListSerializer
from channels.db import database_sync_to_async

def get_users():
    ''' (확실하진 않으나) evaluate를 위해서.. 
        list(~~~)
        이 작업이 없으면 async함수 안에서 users = await database_sync_to_async(get_users)() 로 
        users를 쓸 수 없음 
        ex) print(users) 여기서 에러 발생
    '''        
    users = list(Accounts.objects.prefetch_related('userinroom_set').filter(Q(userinroom__isnull=True)))
    serializer = AccountsSerializer(users, many=True)
    return serializer

def get_rooms():
    rooms = list(Room.objects.all())
    serializer = RoomListSerializer(rooms, many=True)
    return serializer
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
        print("text_data_json:", text_data_json, type(text_data_json))
        space = text_data_json['space']
        if space == 'lobby':
            req = text_data_json['req']
            payload = {"res": req}
            if req == 'getUserList':
                users = await database_sync_to_async(get_users)()
                payload['value'] = users.data
                # Send message to room group
            elif req == 'getRoomList':
                rooms = await database_sync_to_async(get_rooms)()
                payload['value'] = rooms.data
            await self.group_send('send_message', payload)

        elif space == 'room':
            await database_sync_to_async(game_start)(self.room_name)
            await self.group_send('send_message', 'game started')

    # Receive message from room group
    async def send_message(self, event):
        print("event:", event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            event['payload']
        ))

    def group_send(self, type_, payload):
        return self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type_,
                'payload': payload,
            }
        )