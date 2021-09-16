from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Accounts
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

# Create your views here.

@api_view(['POST'])
def signup(request): #회원가입하고 유저 정보 바로 리턴
    print("유저 임시 로그인(생성)")
    now = datetime.datetime.now()
    new_user = Accounts.objects.create(user_name=request.data.get('user_name'), time_to_expire=now)
    print(new_user.user_name)

    return Response({"user_name": new_user.user_name})

@api_view(['POST'])
def check_duplication(request):
    print("아이디 중복 확인")
    user_name = request.data.get('user_name')
    print("아이디는"+user_name)
    try:
        # 중복 검사 실패
        existing_name = Accounts.objects.get(user_name=user_name)
    except:
        # 중복 검사 성공
        existing_name = None
    if existing_name is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    print("중복 검사 완료")
    return JsonResponse(context)




