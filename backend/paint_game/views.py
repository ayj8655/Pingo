# from backend.accounts import models
import shutil
import os
from django.db.models.query_utils import Q
from django.shortcuts import get_list_or_404, get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .serializers import (
    RoomMemberSerializer,
    RoomListSerializer,
    MakeRoomSerializer,
    PaintSerializer,
    PaintSerializer2,
    CategorySerializer,
    ScoreSerializer,
)
from .models import Categories, Score, Room, UserInRoom, Paint
from accounts.models import Accounts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import F

# ayj
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
    "crescent": 6,
    "diamond": 7,
    "icecream": 8,
    "strawberry": 9,
    "t-shirt": 10,
}
model2 = tf.keras.models.load_model("./models/pingo_256_500_0.981_0.099.h5")
###### chat 테스트
from django.shortcuts import render


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
    # print("방 만들기")
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
    return Response(serializer.data)

@swagger_auto_schema(
    method="delete",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "room_id": openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
)
@api_view(["DELETE"])
def delete_room(request):
    # print("방 폭☆파")
    room_id=request.data.get("room_id")
    Room.objects.filter(room=room_id).delete()
    return Response({'detail': '삭제 성공'})

@api_view(["GET"])
def room_list(request):  # 수정요망
    # print("방 리스트 받아오기")
    rooms = Room.objects.all()
    serializer = RoomListSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def room_info(request, room_id):
    # print("방 받아오기")
    room = Room.objects.get(room_id = room_id)
    serializer = RoomListSerializer(room)
    # print(serializer.data)
    return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "room_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "room_password": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
)
@api_view(["POST"])
def enter_room(request):
    # print("방 입장")
    user_id = request.data.get("user_id")
    room = get_object_or_404(Room, room_id=request.data.get("room_id"))
    if room.is_locked == True and room.room_password != request.data.get(
        "room_password"
    ):
        # print("비밀번호가 틀립니다")
        return Response({"detail": "비밀번호가 틀립니다."}, status=status.HTTP_401_UNAUTHORIZED)
    if not UserInRoom.objects.filter(room=room, user_id=user_id).exists():
        UserInRoom.objects.create(room=room, user_id=user_id)
    return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def leave_room(request):
    # print("방 퇴장")
    user_id=request.data.get("user_id")
    room_id=request.data.get("room_id")
    UserInRoom.objects.filter(room=room_id, user_id=user_id).delete()
    return Response({'detail': '삭제 성공'})

@api_view(["GET"])
def room_member(request, room_id):
    # print("방 인원 출력")
    users_in_room = get_list_or_404(UserInRoom, room=room_id)
    serializer = RoomMemberSerializer(users_in_room, many=True)
    # return Response(status=status.HTTP_200_OK)
    return Response(serializer.data)

@api_view(["GET"])
def room_headcount(request, room_id):
    # print("방 인원 출력")
    users_in_room = get_list_or_404(UserInRoom, room=room_id)
    headcount = len(users_in_room)
    return Response({'headcount' : headcount})
    
@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "category_number",
            openapi.IN_QUERY,
            "request쿼리에 요청할 카테고리 갯수를 적는다",
            type=openapi.TYPE_NUMBER,
        ),
    ],
)
@api_view(["GET"])
def get_categories(request):
    try:
        number = int(request.GET.get("category_number", 5))
    except ValueError:
        return Response(
            {"detail": "category_number must be number"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    categories = Categories.objects.order_by("?")[:number]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="post", request_body=PaintSerializer)
@api_view(["POST"])
def saving(request):
    # request.data['category']가 str이기 때문에 PK로 바꿔주는 작업
    request.data["category"] = category_dict[request.data["category"]]
    paint = Paint.objects.filter(
        user=request.data["user"],
        room=request.data["room"],
        category=request.data["category"],
    )
    if paint.exists():  # 이미 존재하면 레코드 삭제
        paint.delete()
    serializer = PaintSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        # print("저장 실패")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method="get")
@api_view(["GET"])
# 사람들의 그림 조회
def paints_of_round(request, room_id, category):
    # 방번호와 카테고리를 params로 받아서 그림들을 조회 , 카테고리가 각 라운드를 의미함
    paints = Paint.objects.filter(room=room_id, category=category_dict.get(category))
    serializer = PaintSerializer2(paints, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user_name": openapi.Schema(type=openapi.TYPE_STRING),
            "room_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "category": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
)
@api_view(["POST"])
def ayj(request):
    # model = tf.keras.models.load_model("./models/pingo_96_28.h5")
    # model = tf.keras.models.load_model("./models/pingo_256_500_0.981_0.099.h5")
    IMG_SIZE = (300, 300)
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
    room_id = request.data.get("room_id")
    user_name = request.data.get("user_name")
    category = request.data.get("category")
    test_path = f"./media/room_{room_id}/{category}/{user_name}.jpg"
    img = tf.keras.preprocessing.image.load_img(
        # test_path, target_size=IMG_SIZE, color_mode="grayscale"
        test_path,
        target_size=IMG_SIZE,
        color_mode="rgb",
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # predictions = model.predict(img_array)
    predictions = model2(img_array)
    # score = tf.nn.softmax(predictions[0])

    # 내가 그린게 가장 높게 예측된 클래스
    max_class = class_names[np.argmax(predictions[0])]
    max_score = np.max(predictions[0]) * 100

    idx = category_dict[category]-1
    # 해당 카테고리의 점수(예측률)
    score = predictions[0][idx] * 100
    score = score.numpy()
    # 점수 누적
    user = get_object_or_404(Accounts, user_name=user_name)
    room = get_object_or_404(Room, room_id=room_id)
    score_obj = Score.objects.filter(room=room_id, user=user)
    if score_obj.exists():
        score_obj.update(score=F("score") + score)
    else:
        Score.objects.create(room=room, user=user, score=score)

    # print(
    #     "원본은 {} 추측은 {} with a {:.2f} percent confidence.".format(
    #         category, class_name, score
    #     )
    # )
    # 파일 복사
    if score >= 80.0:
        dir_path = f"./media/dataset/success/{category}/"
    else:
        dir_path = f"./media/dataset/unsuccessful/{category}/"
    os.makedirs(dir_path, exist_ok=True)
    numbers = len(os.listdir(dir_path))
    shutil.copy(test_path, dir_path+f"new_{category}_{numbers}.jpg")
    return Response({"class_name": category, "score": score, "max_class": max_class, "max_score": max_score})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "room_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    ),
)
@api_view(["POST"])
def game_end(request):
    room_id = request.data.get("room_id")
    user_id = request.data.get("user_id")
    directory = f"./media/room_{room_id}"
    try: 
        # room_n 디렉토리 제거
        shutil.rmtree(directory)
    except OSError as e:
        pass
        # return Response({"detail": f"Error: {e.filename} - {e.strerror}."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
        scores = Score.objects.filter(room_id=room_id).order_by('-score')
        serializer = ScoreSerializer(scores, many=True)
        room = Room.objects.get(room_id=room_id)
        # room의 시작상태가 true면 false로 전환
        if room.is_started == True:
            room.is_started = False
            room.save()
        paint_set = room.paint_set.filter(user_id=user_id)
        # room을 fk로 갖는 자신의 paints 삭제
        if paint_set.exists():
            paint_set.delete()
        return Response(serializer.data)

    except Room.DoesNotExist as e:
        return Response({"detail": "Room matching query does not exist"},  status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get")
@api_view(["GET"])
def result_score(request, room_id):
    # 방번호를 받아서 유저들의 최종 스코어를 순서대로 나열
    score = Score.objects.filter(room_id = room_id).order_by('-score')
    serializer = ScoreSerializer(score, many=True)
    return Response(serializer.data)