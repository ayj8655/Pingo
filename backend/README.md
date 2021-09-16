`python manage.py migrate` 로 db 테이블 생성

가상환경(anaconda envs) 내용 저장
`conda env export > conda_requirements.txt`
conda환경 설치
`conda env create -f conda_requirements.txt`

pip 내용만 저장
`pip freeze > requirements.txt`
가상환경에 패키지 설치
`pip install -r requirements.txt`
목록에 해당하는 패키지 삭제
`pip uninstall -r requirements.txt`


## Conventions

디버그용 print 쓰기

- views 함수 진입하는 곳 최상단에 `print('함수 이름')`
- 서비스 작동하는 위치에서 print

## Naming Conventions

### - 피해야 하는 이름

- '`l`'(소문자), '`O`'(대문자) 또는 '`I`'(대문자) 문자를 단일 문자 변수 이름으로 사용하지 않도록 한다
- 클래스 명은 `카멜케이스(CamelCase)`로 작성
- 함수, 변수명은  snake case (소문자)