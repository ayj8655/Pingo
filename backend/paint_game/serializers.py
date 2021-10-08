from django.db.models import fields
from accounts import models
from rest_framework import serializers
from .models import Room,Ranking,UserInRoom,Words, Paint

class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInRoom
        fields = ('room', 'user')

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MakeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'
