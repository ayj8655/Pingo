pip 내용만 저장
`pip list --format=freeze > requirements.txt`
가상환경에 패키지 설치
`pip install -r requirements.txt`
목록에 해당하는 패키지 삭제
`pip uninstall -r requirements.txt`

가상환경(anaconda envs) 내용 저장
`conda list --export > requirements_conda.txt`

conda패키지 설치
`conda install --file requirements_conda.txt`

❗❗ pip install로 설치한 패키지도 `conda list --export` 시에 기록되는데,

이 중에서 conda install로 설치가 불가능한 패키지들이 있음 (ex: pyjwt, django > 3.x , djangorestframework, numpy==1.19.5 등등)

이런 것들의 목록이 콘솔에 나오기 때문에 주석 처리하고 설치하면 됨

<br>

`python manage.py migrate` 로 db 테이블 생성


## Conventions

디버그용 print 쓰기

- views 함수 진입하는 곳 최상단에 `print('함수 이름')`
- 서비스 작동하는 위치에서 print

## Naming Conventions

### - 피해야 하는 이름

- '`l`'(소문자), '`O`'(대문자) 또는 '`I`'(대문자) 문자를 단일 문자 변수 이름으로 사용하지 않도록 한다
- 클래스 명은 `카멜케이스(CamelCase)`로 작성
- 함수, 변수명은  snake case (소문자)