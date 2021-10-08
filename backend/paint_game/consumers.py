import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime

from django.db.models.query_utils import Q
from accounts.models import Accounts
from .models import Room, UserInRoom, Paint, Categories
from .serializers import RoomListSerializer, CategorySerializer, RoomMemberSerializer2
from accounts.models import Accounts
from accounts.serializers import AccountsSerializer
from channels.db import database_sync_to_async

class Consumer(AsyncWebsocketConsumer):
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
        # print("[consumer-receive] text_data_json:", text_data_json, type(text_data_json), f'room: {self.room_name}')
        space = text_data_json['space']
        req = text_data_json['req']
        payload = {'res': req}
        if space == 'lobby':
            if req == 'getLobbyUsers':
                value = await database_sync_to_async(get_lobby_users)()
                payload['value'] = value
            elif req == 'getRoomList':
                value = await database_sync_to_async(get_rooms)()
                payload['value'] = value

        elif space == 'room':
            if req == 'chat':
                value = text_data_json['value']
                payload['value'] = value
            elif req == 'getRoomUsers':
                value = await database_sync_to_async(get_room_users)(self.room_name)
                payload['value'] = value
            elif req == 'gameStart':
                value = await database_sync_to_async(game_start)(self.room_name, text_data_json['parameter'])
                payload['value'] = value
            elif req == 'roomOwnerQuit':
                await database_sync_to_async(remove_room)(self.room_name)
                await self.group_send('room_owner_quit', payload)
                return
        # Send message to room group
        await self.group_send('send_message', payload)

    # Receive message from room group
    async def send_message(self, event):
        # print("event:", event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            event['payload']
        ))
    async def room_owner_quit(self, event):
        await self.close()

    def group_send(self, type_, payload):
        return self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type_,
                'payload': payload,
            }
        )


def get_lobby_users():
    ''' (확실하진 않으나) evaluate를 위해서.. 
        list(~~~)
        이 작업이 없으면 async함수 안에서 users = await database_sync_to_async(get_users)() 로 
        users를 쓸 수 없음 
        ex) print(users) 여기서 에러 발생
        but, serializer에 쿼리셋을 집어넣으면 괜찮다; 아마 집어넣는대서 evaluate가 되는거 같음
    '''        
    users = Accounts.objects.prefetch_related('userinroom_set').filter(Q(userinroom__isnull=True))
    serializer = AccountsSerializer(users, many=True)
    return serializer.data

def get_room_users(room_id):
    users = UserInRoom.objects.filter(room_id=room_id)
    serializer = RoomMemberSerializer2(users, many=True)
    return serializer.data
    
def get_rooms():
    rooms = Room.objects.all()
    serializer = RoomListSerializer(rooms, many=True)
    return serializer.data

def game_start(room_num, user_name):
    room = Room.objects.get(room_id = room_num)
    if room.room_owner.user_name == user_name:
    # 방에 들어있던 점수들 모두 삭제
        room.score_set.all().delete()
        room.is_started = True
        room.save()
        categories = Categories.objects.order_by("?")[:room.problems]
        serializer = CategorySerializer(categories, many=True)
        return serializer.data
    else:
        return {'error': 'no authority'}

def remove_room(room_num):
    room = Room.objects.filter(room_id=room_num)
    room.delete()
