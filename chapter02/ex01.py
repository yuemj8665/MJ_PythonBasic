import random

# 무작위 난수 생성
ranNum = random.sample(range(1,100), 1)
print("난수 : ", ranNum)

# 난수 testNum 변수에 저장
testNum = ranNum[0]

# 기억력 테스트 게임 시작
print("당신의 기억력을 테스트 합니다")
print("준비 되셨습니까?")
print("1. yes / 2. no")

inputNum = int(int(input()))
type(inputNum)

if inputNum == 1:
    # 난수를 가리기 위해 공백 문자는 20번 출력한다.
    for i in range(20):
        print()
        print("난수는?")
        myNum = int(input())

        # 사용자 입력 수와 난수 비교
        if myNum == testNum:
            print("빙고~ 훌륭합니다!")

        else:
            print("아쉽습니다.")

else:
    print("게임을 종료합니다.")