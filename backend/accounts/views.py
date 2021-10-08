from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Accounts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime
import re

signReg = re.compile(r'^[0-9a-zA-zㄱ-ㅎㅏ-ㅣ가-힣]{3,8}$')
# Create your views here.

r_body_user = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_name': openapi.Schema(type=openapi.TYPE_STRING,),
    }
)

@swagger_auto_schema(method='post', request_body=r_body_user)
@api_view(['POST'])
def signup(request): #회원가입하고 유저 정보 바로 리턴
    # print("유저 임시 로그인(생성)")
    now = datetime.datetime.now() + datetime.timedelta(hours=1)
    # print('request', request.data)
    user_name = request.data.get('user_name')
    flag = bool(signReg.match(user_name))
    if flag:
        new_user = Accounts.objects.create(user_name=user_name, time_to_expire=now)
        return Response({"user_name": new_user.user_name, "user_id":new_user.user_id})
    else:
        return Response({"detail":"invaild input"}, status=status.HTTP_400_BAD_REQUEST)
@swagger_auto_schema(method='delete', request_body= openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_id': openapi.Schema(type=openapi.TYPE_INTEGER,),
    }
))
@api_view(["DELETE"])
def delete(request): #회원삭제
    # print("유저 로그아웃(삭제)")
    Accounts.objects.filter(user_id=request.data.get('user_id')).delete()
    return Response({"detail": '유저 삭제 완료'})

@swagger_auto_schema(method='post', request_body=r_body_user)
@api_view(['POST'])
def check_duplication(request):
    # print("아이디 중복 확인")
    user_name = request.data.get('user_name')
    # print("아이디는"+user_name)
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
    # print("중복 검사 완료")
    return JsonResponse(context)




