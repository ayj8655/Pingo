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

    for category in categories :
        if os.path.isdir("/home/new_jenkins/jenkins/workspace/k-test/backend/media/dataset/success/"+category) :
            amount += len(os.listdir("/home/new_jenkins/jenkins/workspace/k-test/backend//media/dataset/success/"+category))

    if amount > 1000 :
        email = EmailMessage(
            '[PINGO] 분류 성공 이미지 누적 안내',  # 제목
            '현재' + str(amount) + '개의 이미지가 있습니다. 이미지를 GPU 서버로 옮겨서 테스트 해주십시오',
            to=['rlatjsd0603@naver.com'],  # 받는 이메일 리스트
        )
        email.send()
    else :
        email = EmailMessage(
            '[PINGO] 분류 성공 이미지 누적 안내',  # 제목
            '현재' + str(amount) + '개의 이미지가 있습니다. 이미지가 더 누적되기를 기다려 주세요',
            to=['rlatjsd0603@naver.com'],  # 받는 이메일 리스트
        )
        email.send()
        # os.makedirs("/home/jenkins/workspace/test/backend/media/dataset/success/", exist_ok=True)
