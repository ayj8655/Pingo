from django.db import models
from accounts.models import Accounts
# Create your models here.
class Words(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)

class Ranking(models.Model):
    rank = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    score = models.FloatField()

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_owner = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=50)
    room_password = models.CharField(max_length=50, null=True)
    problems = models.IntegerField()
    max_head_counts = models.IntegerField()
    is_locked = models.BooleanField()
    is_started = models.BooleanField()

class UserInRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)

def get_name(instance, filename):
    return f'room_{instance.room.room_id}/{instance.category.word}/{instance.user.user_name}.png'
class Paint(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    category = models.ForeignKey(Words, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_name)