# Step09_Quiz.py

'''
    비밀 번호를 입력 받아서 입력한 비밀 번호가 8자 이상이면 
    "사용 가능한 비밀 번호 입니다"
    그렇지 않으면 
    "사용 불가 입니다" 
    를 출력하는 간단한 프로그래밍을 해보새요
    - hint : len()
'''

password: str = input("비밀번호를 입력하세요: ")

if len(password) >= 8:
    print("사용 가능한 비밀번호 입니다")
else:
    print("사용 불가 입니다")