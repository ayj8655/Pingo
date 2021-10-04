from django.db import models
from .models import Accounts
from rest_framework import serializers
class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('user_id', 'user_name')