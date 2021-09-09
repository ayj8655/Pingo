from .models import Accounts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.

@api_view(['GET'])
def signup(request):
    print("~~의 xx함수")
    now = datetime.datetime.now()
    new_user = Accounts.objects.create(user_name="park2", time_to_expire=now)
    print(new_user.user_name)
    return Response({"greeting": f'{new_user.user_name}님 안녕하세요'})


