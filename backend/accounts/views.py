from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Accounts
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

# Create your views here.

@api_view(['POST'])
def signup(request):
    print("유저 임시 로그인(생성)")
    now = datetime.datetime.now()
    new_user = Accounts.objects.create(user_name=request.data.get('user_name'), time_to_expire=now)
    print(new_user.user_name)
    return Response({"greeting": f'{new_user.user_name}님 안녕하세요'})

@api_view(['POST'])
def check_duplication(request):
    print("아이디 중복 확인")
    user_name = request.data.get('user_name')
    print("아이디는"+user_name)
    user = get_object_or_404(Accounts, user_name=user_name)
    print("유저 이미 존재")
    if(type(user) == Accounts):
        print("type is Accounts")
    # serializer = UserProfileSerializer(user)
    return Response({"result": "duplicate user name"})



