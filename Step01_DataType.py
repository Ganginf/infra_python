# 한줄 주석입니다.

"""
    여기서부터 주석입니다.
    어쩌구 저쩌구 블라블라..
"""

print("Step01 시작")

# python의 여러가지 데이터 type에 대해서 알아보자 

# int type(정수)
num1 = 10
# float type(실수)
num2 = 10.1

# str type
myName = '김현경'
yourName = "아톰"
ourName = """
    KT Cloud Infra    
    화이팅!
"""

# 순서가 중요한 여러개의 데이터를 관리하고 싶다면...
# 내가 좋아하는 음식 목록 3가지를 하나의 변수에 순서대로 담고 싶다면...
food1 = "떡볶이" 
food2 = "미더덕"
food3 = "곱창"
foods = ["삼겹살","김밥","닭발"]  #List type

print(foods)

# 순서가 중요치 않지만 여러개의 데이터를 관리하고 싶다면...
# 회원 1명의 정보
num=1
name="김구라"
addr="노량진"

mem1 = {"num":1, "name":"김구라", "addr":"노량진"} #dict type

print(mem1)


# 순서가 중요치 않은 데이터를 하나의 묶음으로 관리(키값 없이)
mySet = {"빨강사탕", "초록사탕", "노랑사탕"} #Set Type

print(mySet)

# 특정 Code 블럭을 필요한 시점에 일괄 실행하고 싶다면?

#함수를 만들고
def store():
    print("냉장고 문을 연다")
    print("물건을 저장한다")
    print("냉장고 문을 닫는다")

#여기서는 바로 실행 했지만 필요한 시점에 실행된다.
store()
returnValue = store()


# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶다면? None
a = None
print("어떤 작업을 하고")
print("필요할 때 값을 넣는다")
a = "테스트"


# 참과 거짓을 나타내는 data type (Bool)
isMan=True
isWoman=False
isDifferent=True
isRun=False
