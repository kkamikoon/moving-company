# API 사용방법

## URL 목록
* ~/admin/
* api/moving-company/
* api/moving-company/\<int:pk>/
* api/moving-reservation/
* api/moving-reservation/\<int:pk>
* api/customer-information/
* api/customer-information/\<int:pk>
* api/customer-feedback/
* api/customer-feedback/\<int:pk>

## 라이브러리

### apt install
```bash
$ apt install -y libmysqlclient-dev docker docker-compose
```

### pip install
```bash
$ pip3 install django djangorestframework mysqlclient
```

# 실행방법
```bash
python3 manage.py runserver x.x.x.x:yy

# IP : x.x.x.x 
# PORT : yy
```

## Admin 계정 생성
```bash
$ python3 manage.py createsuperuser

# make your account root / root
# Test Account : root / toor
```

## Admin 페이지
* `~/admin/` 경로로 들어가서, 방금 생성한 계정을 통해 어드민 로그인을 한다.
* 해당 페이지에서 `데이터를 추가`할 수 있다.

## REST framework
### \<your-ip-or-domain>/api/\<api-path>/

* 모든 이사회사들의 리스트를 반환해주는 API의 예시
* example > `http://???/api/moving-company/`


```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "total_data_count": 2,
    "result": [
        {
            "name": "이사회사1",
            "tel": "010-1111-1**1",
            "address": "서울 동작구 신대방동",
            "reservation_status": true
        },
        {
            "name": "이사회사2",
            "tel": "010-2222-2**2",
            "address": "서울 동작구 신대방동",
            "reservation_status": true
        }
    ]
}
```

### \<your-ip-or-domain>/api/\<api-path>/\<int:pk>
* 특정 이사회사의 정보를 반환해주는 API의 예시
* example > `http://???/api/moving-company/1/`
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "이사회사1",
    "tel": "010-1111-1**1",
    "address": "서울 동작구 신대방동",
    "reservation_status": true
}
```

# Docker
## Quick Start
### docker-compose.yml 수정하기
원하는 포트 번호로 변경하여 접근할 수 있도록 한다.
```docker
version: "3.3"

services:
    web:
        build: .
        volumes:
            - .:/pg
        command: python manage.py runserver 0.0.0.0:8000
        ports:
            - "80:8000" # port 80(outside) -> 8000(inside of docker)
```

```bash
# pg 디렉토리로 들어간다.
$ cd pg/

# ~pg/ 디렉토리에서 docker-compose 명령 실행
$ docker-compose up -d
```

### docker로 접속
연결한 정보를 통해 도커로 접속한다.

예시 > http://???/admin/
```
예제 Django Administration 정보

ID : root
PW : toor
```

