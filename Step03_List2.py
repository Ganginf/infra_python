#list type 에 대해서 알아보기 

nums = [10, 20, 30, 40, 50]
names = ["kim","park", "jo", "oh", "cohi"]

# list에 들어 있는 데이터를 앞에서 부터 순서대로 참조하면서 어떤 동작을 할 일들이 많이 발생한다. 
for item in nums:
    print(item)

# names 에 들어 있는 데이터를 앞에서 부터 순서대로 참조하면서 출력
for item in names:
    print("names를 순서대로 출력중...")
    print(item)

r1 = range(5)
r2 = range(10)

print(r1)
print(r2)

for item in range(5):
    print(item)

length1 = len(names)


# result2에 들어 가는 값을 예상해 보세요.
result2 = range(len(name))

# 반복문을 돌면서 인덱스도 같이 필요하다면...
for i in range(len(name)):
    print("list의 index와 함께 출력합니다.")
    print(i, names[1])

print("종료합니다")
