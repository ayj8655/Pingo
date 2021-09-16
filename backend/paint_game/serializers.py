from rest_framework import serializers
from .models import Room,Ranking,UserInRoom,Words

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


