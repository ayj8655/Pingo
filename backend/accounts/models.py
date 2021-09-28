from django.db import models

# Create your models here.
class Accounts(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    time_to_expire = models.DateTimeField()
