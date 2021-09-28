# from backend.accounts import models
from django.shortcuts import get_list_or_404, get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from .serializers import (
    RoomMemberSerializer,
    RoomListSerializer,
    MakeRoomSerializer,
    PaintSerializer,
)
from .models import Paint, Words, Ranking, Room, UserInRoom

from .serializers import (
    RoomMemberSerializer,
    RoomListSerializer,
    MakeRoomSerializer,
    PaintSerializer,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps

# ayj
import os
import tensorflow as tf
import numpy as np

# ayj


# Create your views here.
category_dict = {
    "banana": 1,
    "bulb": 2,
    "calculator": 3,
    "carrot": 4,
    "clock": 5,
    "crecent": 6,
    "diamond": 7,
    "icecream": 8,
    "strawberry": 9,
    "t-shirt": 10,
}

###### chat 테스트
from django.shortcuts import render

from paint_game import serializers


def index(request):
    return render(request, "paint_game/index.html")


def room(request, room_name):
    return render(request, "paint_game/room.html", {"room_name": room_name})


#######


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "room_owner": openapi.Schema(type=openapi.TYPE_STRING),
            "room_name": openapi.Schema(type=openapi.TYPE_STRING),
            "room_password": openapi.Schema(type=openapi.TYPE_STRING),
            "problems": openapi.Schema(type=openapi.TYPE_INTEGER),
            "max_head_counts": openapi.Schema(type=openapi.TYPE_INTEGER),
            "is_locked": openapi.Schema(type=openapi.TYPE_BOOLEAN),
            "is_started": openapi.Schema(type=openapi.TYPE_BOOLEAN),
        },
    ),
)
@api_view(["POST"])
def make_room(request):  # 만들어준 방의 정보 return
    print("방 만들기")
    print(request.data)
    accounts_model = apps.get_model("accounts", "Accounts")
    room_owner = get_object_or_404(
        accounts_model, user_name=request.data.get("room_owner")
    )
    new_room = Room.objects.create(
        room_owner=room_owner,
        room_name=request.data.get("room_name"),
        room_password=request.data.get("room_password"),
        problems=request.data.get("problems"),
        max_head_counts=request.data.get("max_head_counts"),
        is_locked=request.data.get("is_locked"),
        is_started=request.data.get("is_started"),
    )
    serializer = MakeRoomSerializer(new_room)
    print("방 만들기 완료")
    return Response(serializer.data)


@api_view(["GET"])
def room_list(request):  # 수정요망
    print("방 리스트 받아오기")
    rooms = get_list_or_404(Room)
    print("rooms 받아옴")
    serializer = RoomListSerializer(rooms, many=True)
    print("방 리스트 받아오기 완료")
    return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "room_id": openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
)
@api_view(["POST"])
def enter_room(request):
    print("방 입장")
    accounts_model = apps.get_model("accounts", "Accounts")
    user = get_object_or_404(accounts_model, user_id=request.data.get("user_id"))
    room = get_object_or_404(Room, room_id=request.data.get("room_id"))
    new_user_in_room = UserInRoom.objects.create(room=room, user=user,)
    print("방 입장 완료")
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def room_member(request, room_id):
    print("방 인원 출력")
    users_in_room = get_list_or_404(UserInRoom, room=room_id)
    print(users_in_room)
    serializer = RoomMemberSerializer(users_in_room, many=True)
    print("방 인원 출력 완료")
    # return Response(status=status.HTTP_200_OK)
    return Response(serializer.data)


@swagger_auto_schema(method="post", request_body=PaintSerializer)
@api_view(["POST"])
def saving(request):
    serializer = PaintSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print("저장 실패")
        return Response(serializer.errors)


@swagger_auto_schema(method="get")
@api_view(["GET"])
def paints_of_round(request, room_id, category):
    paints = Paint.objects.filter(room=room_id, category=category_dict.get(category))
    serializer = PaintSerializer(paints, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def ayj(request):
    model = tf.keras.models.load_model("./models/pingo_96_28.h5")
    IMG_SIZE = (100, 100)
    class_names = [
        "banana",
        "bulb",
        "calculator",
        "carrot",
        "clock",
        "crescent",
        "diamond",
        "icecream",
        "strawberry",
        "t-shirt",
    ]

    test_path = "./media/room_1/banana/안영진_ZPcNQa3.png"
    img = tf.keras.preprocessing.image.load_img(
        test_path, target_size=IMG_SIZE, color_mode="grayscale"
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(predictions)
    print(predictions[0])
    print(score)

    print(
        "원본은 banana 추측은 {} with a {:.2f} percent confidence.".format(
            class_names[np.argmax(score)], 100 * np.max(score)
        )
    )

    return Response(
        {"score": 100 * np.max(score), "class_name": class_names[np.argmax(score)]}
    )

