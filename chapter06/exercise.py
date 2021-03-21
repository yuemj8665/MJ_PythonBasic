import random

# 무작위 난수 생성
ranNum = random.sample(range(1,3),1)
user01winrate = 0
user02winrate = 0


# 난수를 comNum 변수에 저장
comNum = ranNum[0]

print("홀짝게임. 1. 홀    2. 짝")

print("첫 번쨰 사용자 문자 입력")
user01Num = int(input())
print("두 번쨰 사용자 문자 입력")
user02Num = int(input())

if(user01Num%2) == (comNum%2):
    print("첫 번쨰 사용자는 O")
    user01winrate = 1
else:
    print("첫 번쨰 사용자는 X")
    user01winrate = 0
    
if(user02Num%2) == (comNum%2):
    print("두 번쨰 사용자는 O")
    user02winrate = 1

else:
    print("두 번쨰 사용자는 X")
    user02winrate = 0

print('컴퓨터 숫자 : ')
print(comNum)

if user01winrate == user02winrate :
    print("비겼습니다")
elif user01winrate > user02winrate :
    print("첫 번쨰 사용자가 이김")
elif user02winrate > user01winrate :
    print("두 번쨰 사용자가 이김")
    