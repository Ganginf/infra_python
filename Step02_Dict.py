# dict type 에 대하여 알아보자 

"""
    -dict type
    1. key:value 형태로 데이터를 저장한다.
    2. 순서가 없는 데이터이다.
    3.Key 값을 이용해서 저장된 값을 참조한다.
"""

#회원 1명의 데이터 
mem1 ={"num":1, "name":"Kimhyun","isMan":True}
#회원 1명의 데이터(사용이 불편하다)
#infol = [1,"Kimhyun",True]
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

a = (mem1["num"])
b = (mem1["name"])
c = (mem1["isMan"])

# dict 안의 내용을 수정하기 
mem1["num"]=2
mem1["name"]="Atom"
mem1["isMan"]=False


#특정 Key 값으로 저장된 내용 삭제
del mem1["isMan"]

#모든 값 삭제 
mem1.clear()


print("종료됩니다.")