# 경계선
lien = "============================="

# 변수를 선언하고 문자('h')와 문자열('hello')를 변수에 담는다
str1 = 'h'
str2 = 'hello'

# type() 함수를 이용하여 변수에 담겨있는 데이터 타입을 확인한다.
print(type(str1))
print(type(str2))

print(lien)

# 데이터를 변수에 담지 않고 type() 함수를 이용해서 데이터 타입을 확인한다
print(type('h'))
print(type('hello'))

print(lien)

# 숫자도 작은 따옴표(')로 묶으면 문자(열)로 취급한다.
print(type('1'))
print(type('12312312312312313123123'))