프론트엔드 → Vue, 포트 : 8080

npm install
npm run serve


백엔드 → Django , 포트 : 8000

pip install -r requirements.txt
conda env create -f conda_requirements.txt

python manage.py migrate
python manage.py runserver

DB → Mysql

포트 : 3306


스웨거 링크 : [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

포팅메뉴얼

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
    
6. 데이터베이스 덤프 파일 최신본
    1. [https://velog.io/@finelinefe/TIP-MySQL-Workbench를-이용해-DB-Dump](https://velog.io/@finelinefe/TIP-MySQL-Workbench%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-DB-Dump)
        
        [Dump20211007.sql](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/936f14b1-8e9c-4cfd-bab8-4c9e26249889/Dump20211007.sql)
        
        오후 4시 55분 기준 db
        
7. 시연 시나리오(스크립트 포함)
    1. 시연 순서에 따른 site 화면별, 실행별(클릭 위치 등) 상세 설명
    
    [시연 시나리오.pptx](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ccb72615-995e-47e7-bf04-f7c1d0a81d44/시연_시나리오.pptx)
