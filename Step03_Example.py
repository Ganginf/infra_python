#Step03_Example.py

"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어져 있다
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(data)로 순서대로 관리하고 싶다면...
"""

#3명의 회원 정보를 각각 dict에 담은 다음 dict를 list에 담는 코드를 착성해서 채팅방에 보내세요
mem1 = {"num":1, "name":"파이리", "addr":"서울"}
mem2 = {"num":2, "name":"꼬부기", "addr":"경기"}
mem3 = {"num":3, "name":"피카츄", "addr":"광주"}
# dict 3개를 list에 담기 
members = [mem1, mem2, mem3]
print(members)

a = members 
b = members[0]
c = members[0]["num"]
d = members[0]["name"]

print("종료 합니다")