from django.http import HttpResponse
# from backend.accounts import models
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from .serializers import RoomMemberSerializer,RoomListSerializer,MakeRoomSerializer
from .models import Words,Ranking,Room,UserInRoom
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps


# Create your views here.
@api_view(['POST'])
def make_room(request): #만들어준 방의 정보 return
    print("방 만들기")
    accounts_model = apps.get_model('accounts', 'Accounts')
    room_owner = get_object_or_404(accounts_model, user_name=request.data.get('room_owner'))
    new_room = Room.objects.create(
        room_owner = room_owner,
        room_name = request.data.get('room_name'),
        room_password = request.data.get('room_password'),
        problems = request.data.get('problems'),
        max_head_counts = request.data.get('max_head_counts'),
        is_locked = request.data.get('is_locked'),
        is_started = request.data.get('is_started')
        )
    serializer = MakeRoomSerializer(new_room)
    print("방 만들기 완료")
    return Response(serializer.data)

@api_view(['GET'])
def room_list(request): #수정요망
    print("방 리스트 받아오기")
    rooms = get_list_or_404(Room)
    print("rooms 받아옴")
    serializer = RoomListSerializer(rooms, many=True)
    print("방 리스트 받아오기 완료")
    return Response(serializer.data)

@api_view(['POST'])
def enter_room(request):
    print("방 입장")
    accounts_model = apps.get_model('accounts', 'Accounts')
    user = get_object_or_404(accounts_model, user_id=request.data.get('user_id'))
    room = get_object_or_404(Room, room_id=request.data.get('room_id'))
    new_user_in_room = UserInRoom.objects.create(
        room = room,
        user = user,
    )
    print("방 입장 완료")
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def room_member(request, room_id):
    print("방 인원 출력")
    users_in_room = get_list_or_404(UserInRoom, room=room_id)
    print(users_in_room)
    serializer = RoomMemberSerializer(users_in_room, many=True)
    print("방 인원 출력 완료")
    # return Response(status=status.HTTP_200_OK)
    return Response(serializer.data)
