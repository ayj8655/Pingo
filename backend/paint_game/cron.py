from django.core.mail import EmailMessage

def update():
    print("업데이트 알림 시작")
    email = EmailMessage(
        '장고 이메일 테스트',  # 제목
        '이것은 테스트 이메일 입니다',  # 내용
        # 'from@example.com',  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
        to=['rlatjsd0603@naver.com'],  # 받는 이메일 리스트
    )
    email.send()
    print("업데이트 알림 끗")