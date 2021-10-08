from django.core.files import storage
from django.db import models
from accounts.models import Accounts
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def get_name(instance, filename):
    return f'room_{instance.room.room_id}/{instance.category.category}/{instance.user.user_name}.jpg'
    
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Categories(models.Model):
    word_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_owner = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=50)
    room_password = models.CharField(max_length=50, null=True)
    problems = models.IntegerField()
    max_head_counts = models.IntegerField()
    is_locked = models.BooleanField()
    is_started = models.BooleanField()

class Score(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class UserInRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)

class Paint(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_name, storage=OverwriteStorage())
