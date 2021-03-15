# 경계선
line = "================================"
# 변수를 선언하고 음수, 0, 양수를 각각 변수에 담는다
iNum1 = -1234567890
iNum2 = 0
iNum3 = 1234567890

# type함수를 이용하여 각 변수에 담긴 데이터 타입을 확인한다
print(type(iNum1))
print(type(iNum2))
print(type(iNum3))

# 경계선
print(line)

# 데이터를 변수에 담지 않고 type() 함수를 사용하여 데이터 타입을 확인한다
print(type(-1234567890))
print(type(0))
print(type(1234567890))

print(line)

# 데이터를 연산한 결과에 대해서도 type() 함수를 이용 할 수 있다.
print(type(10+100))
print(type(10-100))
print(type(10*100))
print(type(10/100))