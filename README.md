# API Usage

## URL list
* ~/admin/
* api/moving-company/
* api/moving-company/\<int:pk>/
* api/moving-reservation/
* api/moving-reservation/\<int:pk>
* api/customer-information/
* api/customer-information/\<int:pk>
* api/customer-feedback/
* api/customer-feedback/\<int:pk>

## Libraries

### apt install
```bash
$ apt install libmysqlclient-dev
```

### pip install
```bash
$ pip3 install django djangorestframework mysqlclient
```

# Activate
```bash
python3 manage.py runserver x.x.x.x:yy

# IP : x.x.x.x 
# PORT : yy
```

## Admin Create
```bash
$ python3 manage.py createsuperuser

# make your account root / root
# Test Account : root / toor
```

## Admin page
* Access to `~/admin/` and log in using your account just you made.
* You can `add your data` on this page

## REST framework
### \<your-ip-or-domain>/api/\<api-path>/
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