import random

varList = [3,'a','hello',3.14,-12]

# 무작위 난수 생성
ranNum = random.sample(range(0,len(varList)),1)

# 난수를 이용해서 varList의 아이템 추출
print("아래 데이터의 타입은")
print(varList[ranNum[0]])

input()
print("=== 정답 ===")
print(type(varList[ranNum[0]]))