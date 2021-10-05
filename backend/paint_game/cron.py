from django.core.mail import EmailMessage
import os

def update():
    print("업데이트 알림 시작")

    categories = [
        "banana",
        "bulb",
        "calculator",
        "carrot",
        "clock",
        "crecent",
        "diamond",
        "icecream",
        "strawberry",
        "t-shirt",
    ]
    #쌓인 이미지 개수
    amount = 0
    now_dir = os.getcwd()

    for category in categories :
        if os.path.isdir("/home/jenkins/workspace/test/backend/media/dataset/success/"+category) :
            amount += len(os.listdir("/home/jenkins/workspace/test/backend//media/dataset/success/"+category))

    if True :
        email = EmailMessage(
            '[PINGO] 분류 성공 이미지 누적 안내',  # 제목
            '이것은 테스트 이메일 입니다. 현재' + str(now_dir) + '에 있습니다',
            to=['rlatjsd0603@naver.com'],  # 받는 이메일 리스트
        )
        email.send()
        # os.makedirs("/home/jenkins/workspace/test/backend/media/dataset/success/", exist_ok=True)
