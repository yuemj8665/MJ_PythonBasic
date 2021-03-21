myScore = 90
targetScore = 80

# if문
if myScore >= targetScore : # if문을 활용하여 나의 점수와 목표점수를 비교한다
    print('잘했다') # 조건에 만족하므로(True) 실행문이 실행된다.

myScore = 75
targetScore = 80

# if문
if myScore >= targetScore : # if문을 활용하여 나의 점수와 목표점수를 비교한다
    # 조건에 만족하는 경우 (True) 실행문이 실행된다.
    print('잘했다')

else : # else 문을 활용하여 조건에 만족하지 않은 경우(False) else문이 실행된다.
    print('아니다')

# if-elif문
if myScore >= 90:
    print("수")
elif myScore >= 80:
    print("우")
elif myScore >= 70:
    print("미")
elif myScore >= 60:
    print("양")
else :
    print("가")