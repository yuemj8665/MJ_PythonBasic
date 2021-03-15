# 경계선
line = "========================================="

# 변수를 선언하고 실수를 각각의 변수에 담는다
iNum1 = 123.456
iNum2 = 0.0
iNum3 = -123.456

# type() 함수를 사용하여 각 변수에 담긴 데이터 타입을 확인한다.
print(type(iNum1))
print(type(iNum2))
print(type(iNum3))

print(line)

# 데이터를 변수에 담지않고도 type()함수를 사용 할 수 있다.
print(type(123.456))
print(type(0.0))
print(type(-123.123))

print(line)

# 데이터를 연산한 결과에서도 type()함수를 사용 할 수 있다.
print(type(10+123.123))
print(type(10-123.123))
print(type(10*123.123))
print(type(10/123.123))