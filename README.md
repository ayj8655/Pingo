
# 프론트엔드
npm install

npm run serve

---

# 백엔드
pip install -r requirements.txt

conda env create -f conda_requirements.txt

python manage.py migrate

python manage.py runserver



---


#포팅메뉴얼

    
1. 포팅 매뉴얼
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
            
2. 프로젝트에서 사용하는 외부 서비스 정보 문서
    1. 무

3. 현재 AI 모델
   
<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6d0d1b70-988e-4bdb-a786-db7b6970419c/pingo_256_500_0.981_0.099.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T005105Z&X-Amz-Expires=86400&X-Amz-Signature=b03be3c256b9de1e3af273b5a37f0b3d8de07290bf37f28a3a6276f464508c69&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22pingo_256_500_0.981_0.099.png%22" width="500" height="500">

- accuracy = 0.981
- loss = 0.099
