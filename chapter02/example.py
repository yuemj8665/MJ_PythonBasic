import random

# random.sample() 함수를 이용해서 난수를 발생하고, 발생 된 난수를 ranNum 변수에 담는다.
# sample() 함수 안의 range(1,100)은 1부터 100사이(1이상 100미만) 난수 발생을 뜻 한다.
# 1은 난수 1개를 발생시킨다
# random.sample(range(난수 발생 범위), 난수 생성 갯수)
ranNum = random.sample(range(1,100), 1)

# 발생된 난수 출력
print("난수 : ", ranNum)

# 발생된 난수를 testNum 변수에 저장한다.
# random.sample을 이용하여 나온 난수는 list형식으로 반환된다.
# 리스트는 배열과 비슷하며, 난수 하나를 얻기 위해서는 list의 첫 번쨰 인자에 해당하는 데이터를 가져와야 한다.
# 첫 번쨰 인자를 가져오기 위해 ranNum[0]을 사용했고, 이렇게 가져온 난수 하나를 testNum이라는 변수에 담았다.
testNum = ranNum[0]

# 기억력 테스트 게임 시작
print("당신의 기억력을 테스트 합니다")
print("준비 되셨습니까?")
print("1. yes / 2. no")

# 사용자로부터 숫자를 입력받아 게임을 시작할지 종료할지 물어본다.
inputNum = int(input())
type(inputNum)

# 사용자가 입력한 숫자가 1이라면,
if inputNum == 1:
    # 게임을 진행시킨다.
    # 난수를 가리기 위해 공백 문자는 20번 출력한다.
    for i in range(20):
        print()

        # 사용자한테 위에서 발생한 난수를 물어본다.
        print("난수는?")
        # 사용자가 입력한 숫자를 myNum 변수에 담는다.
        myNum = int(input())

        # 사용자 입력 수와 난수 비교
        # 사용자가 입력한 숫자(myNum)와 위에서 발생한 난수(testNum)가 일치하면 빙고
        if myNum == testNum:
            print("빙고~ 훌륭합니다!")

        # 사용자가 입력한 숫자(myNum)와 위에서 발생한 난수(testNum)가 일치하지 않으면 아쉽습니다.
        else:
            print("아쉽습니다.")
            
# 사용자가 입력한 숫자가 1이 아니면 종료한다
else:
    print("게임을 종료합니다.")