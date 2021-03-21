import random

# 무작위 난수 생성
ranNum = random.sample(range(1,3),1)

# 난수를 comNum 변수에 저장
comNum = ranNum[0]

print("홀짝게임. 1. 홀    2. 짝")

userNum = int(input())

if(userNum%2) == (comNum%2):
    print("맞췄습니다")

else:
    print("틀렸습니다")

print('컴퓨터 숫자 : ')
print(comNum)