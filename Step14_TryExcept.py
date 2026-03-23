
# main 으로 실행했을 때 실행할 code 블럭
from turtle import reset


if __name__ == "__main__":
    try:
        #문자열
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")

        #입력한 문자열을 숫자로 형변환
        num1 : int = int(num1_str)
        num2 : int = int(num2_str)

        reset = num2/num1

        #결과를 출력
        print(f"{num2}를 {num1}으로 나눈 결과 값: {reset}")

    except ValueError as ve: # ve에는 에러 정보가 들어 있다. 
        print(ve)

    except ZeroDivisionError as ze: # ze에는 에러 정보가 들어 있다. 
        print(ze)

    #어떤 중요한 마무리 작업을 합니다
        print("중요한 마무리 작업을 합니다.")


        
    
