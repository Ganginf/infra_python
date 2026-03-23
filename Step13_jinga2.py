'''
    Template 문자열을 정의하고 어떤 데이터를 Template 문자열에 전달해서
    결과 문자열을 얻어내는 작업을 jinja2를 이용해서 테스트 해보자

    설치 후 사용 필요 
    pip install jinja2
'''
# 테스트용 tamplate를 만든다 
from jinja2 import Template


my_template = """
    번호: {{num}}
    이름: {{name}}
    주소: {{addr}}
"""

# template에 출력할 데이터를 준비한다. 
mem1 = {"num":1, "name":"김구라", "addr":"노량진"} # dict type
mem2 = {"num":2, "name":"강호동", "addr":"성수동"}

# import한 Template 클래스의 생성자에 my_template 문자열을 넣어서 객체를 생성한다.
temp = Template(my_template)
result1 = temp.render(mem1)
print(result1)

temp = Template(my_template)
result2 = temp.render(mem2)
print(result1)