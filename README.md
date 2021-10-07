#포팅메뉴얼

1. 프로젝트 소스코드 및 빌드파일 → 깃랩
2. 발표자료 - PPT OR PDF 파일 → 에듀싸피>열린게시판>ucc경진대회 팀장대표 제출
3. UCC → MP4 파일
    
    제목명 : 특화PJT_대전2반_B307_안영진
    
    파일명 : 특화PJT_대전2반_B307_안영진
    
4. 포팅 매뉴얼
    1. **gitlab 소스 클론 이후 빌드 및 배포할 수 있는 작업 문서**
        1. 사용한 JVM,웹서버,WAS 제품 등의 종류와 설정값, 버전(ide버전 포함) 기재
            1. 프론트엔드 : Vue(3.0), IDE → VSCode
            2. 백엔드 : Django (3.2.7), IDE → VSCode,PyCharm
            3. AI : Tensorflow 2.4.1
            4. Mysql : 5.7
            5. Redis : 5
            6. Python 3.7.0
            
        2. 빌드 시 사용되는 환경 변수 등의 주요 내용 상세 기재
            1. 프론트엔드 : npm install
            2. 백엔드 : pip install -r requirements.txt
            3. AI : conda install git matplotlib scikit-learn tqdm scipy numpy=1.19 tensorflow-gpu==2.4.1
            
        3. 배포 시 특이사항 기재
            1. 백엔드는 직접 실행해야한다.(자동 배포시 websocket 사용 불가) 
            
            백엔드 서버 종료 : sudo killall daphne
            
            백엔드 서버 기동 : sudo nohup daphne -b 0.0.0.0 -p 8000 backend.asgi:application &
            
            백엔드 서버 프로세스 확인 : ps -ef | grep daphne 
            
            여기서 sudo nohup daphne -b 0.0.0.0 -p 8000 backend.asgi:application & 있는지 확인
            
        4. 데이터베이스 접속 정보 등 프로젝트에 활용되는 주요 계정 및 프로퍼티가 정의된 파일 목록
            1. Mysql ID : root, PW : ssafy
            2. 젠킨스 ID : admin, PW : ssafy
            
5. 프로젝트에서 사용하는 외부 서비스 정보 문서
    1. 무

6. 현재 AI 모델
https://vagabond-loganberry-e23.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6d0d1b70-988e-4bdb-a786-db7b6970419c%2Fpingo_256_500_0.981_0.099.png?table=block&id=57b81cff-9e26-46b4-8746-787ebf7def6e&spaceId=44063e9b-c12e-420e-b997-610d5caef9f8&width=2000&userId=&cache=v2
