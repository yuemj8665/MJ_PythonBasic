import random

# varList변수에 정수, 실수, 그리고 문자(열)가 혼합된 리스트 형식의 데이터를 저장한다
varList = [3, 'a', 'hello', 3.14, -12]

# 무작위 난수 생성
ranNum = random.sample(range(0,len(varList)),1)

# 난수를 이용해서 varList의 아이템 추출
# random.sample() 함수를 이용해서 발생된 난수는 배열 형태이므로 인덱스(0)을 이용해서 난수를 추출하고,
# 이를 이용해서 varList의 데이터 하나를 무작위로 추출한다.
print("아래 데이터 타입은?")
print(varList[ranNum[0]])

# input() 함수를 이용해서 사용자의 정답을 입력받는다.
input()

print("=== 정답 ===")
print(type(varList[ranNum[0]]))