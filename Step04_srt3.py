# yaml 형식의 문자열 다루기 

# yaml 문자열을 다룰때는 외부 모듈을 pip로 설치를 해서 import 해야한다.
info = '''
name: 김현경
addr: 서울
foods: 
  - 맥주
  - 마라탕
isMan: False
Hobby:
  Exercise: 폴댄스
  Travel: 국내여행
'''

# 검색 혹은 ai의 도움을 받아서 info에 들어 있는 문자열을 dict type으로 바꾸세요
# 그런 다음 dict에 들어 있는 내용을 확인 후 다시 dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요. 

import yaml

yaml_str = """
info:
  name: 김현경
  addr: 서울
  foods:
    - 맥주
    - 마라탕
  isMan: False
Hobby:
  Exercise: 폴댄스
  Travel: 국내여행
"""

data = yaml.safe_load(yaml_str)
print(data)
print(type(data)) 

yaml_result = yaml.dump(data, allow_unicode=True, sort_keys=False)
print(yaml_result)
print(type(yaml_result))