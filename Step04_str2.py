# json 모듈 설치하기 

import json
from turtle import reset

#info 는 str type이긴 한데 문자열이 특별한 형식(Json)로 변경된 값을 가지고 있다.

info = '''{
    "name":"김현경",
    "addr":"서울",
    "foods":["마라탕,"치킨]
}'''

# result는 str(json형식)의 문자열이 python 의 dict로 변경된 값을 가지고 있다 
reset = Json.loads(info)

print(reset["name"])
print(reset["addr"])
print(reset["foods"])