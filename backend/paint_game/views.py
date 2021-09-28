from django.http import HttpResponse
from django.http.response import JsonResponse
# from backend.accounts import models
from django.shortcuts import get_list_or_404, get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from .serializers import RoomMemberSerializer,RoomListSerializer,MakeRoomSerializer #, PaintSerializer
from .models import Words,Ranking,Room,UserInRoom #, Paint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.conf import settings
import os
import base64


# Create your views here.
###### chat 테스트
from django.shortcuts import render

from paint_game import serializers
def index(request):
    return render(request, 'paint_game/index.html')
def room(request, room_name):
    return render(request, 'paint_game/room.html', {
        'room_name': room_name
    })
#######

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'room_owner': openapi.Schema(type=openapi.TYPE_STRING),
        'room_name': openapi.Schema(type=openapi.TYPE_STRING),
        'room_password': openapi.Schema(type=openapi.TYPE_STRING),
        'problems': openapi.Schema(type=openapi.TYPE_INTEGER),
        'max_head_counts': openapi.Schema(type=openapi.TYPE_INTEGER),
        'is_locked': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        'is_started': openapi.Schema(type=openapi.TYPE_BOOLEAN),
    }
))
@api_view(['POST'])
def make_room(request): #만들어준 방의 정보 return
    print("방 만들기")
    print(request.data)
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

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        'room_id': openapi.Schema(type=openapi.TYPE_INTEGER),
    }
))
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

@api_view(['POST'])
def canvasToImage(request):
    data = request.data['data']
    # print(request.data)
    # data = request.POST.__getitem__('data')
    # print(data)
    # print("--------------------")
    # print("--------------------")
    # data = data[22:] # 앞의 'data:image/png;base64 부분 제거
    new_data = data + '='*(4 - (len(data) % 4))
    # new_data = data
    new_data = new_data[22:]
    print(new_data)
    number = 1

    # 저장할 경로 및 파일명을 지정
    path = str(os.path.join(settings.BASE_DIR, 'resultImg/'))
    filename = 'image' + str(number) + '.jpg'

    # "wb"(바이너리파일 쓰기전용)으로 파일을 open
    image = open(path + filename, 'wb')
    
    # 'base64.b64decode()'를 통하여 디코딩을 하고 파일에 써준다.
    image.write(base64.b64decode(new_data))
    image.close()
    ################이미지 저장###############
    # django media??

    answer = {'filename': filename}
    return JsonResponse(answer)

# @api_view(['POST'])
# def saving(request):
#     serializer = PaintSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
