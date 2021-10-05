from django.db.models import fields
from accounts.models import Accounts
from rest_framework import serializers
from .models import Room, UserInRoom, Paint, Categories, Score

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('user_name', 'user_id')

class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInRoom
        fields = ('room', 'user')

class RoomMemberSerializer2(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    class Meta:
        model = UserInRoom
        fields = ('user',)

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category',)

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('score', 'user')
        depth = 1
