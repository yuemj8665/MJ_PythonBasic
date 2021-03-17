# 사용자가 입력할 첫 번째 숫자를 firstNum 변수에 담는다
firstNum = input()
# 사용자가 입력할 연산자를 operator 변수에 담는다
operator = input()
# 사용자가 입력할 두 번째 숫자를 secondNum 변수에 담는다
secondNum = input()

if operator == '+': # 덧셈이라면
    print("덧셈 연산 결과")
    print(int(firstNum)+int(secondNum))
elif operator == '-': # 뺄셈이라면
    print("뺄셈 연산 결과")
    print((int(firstNum)-int(secondNum)))
elif operator == '*': # 곱셈이라면
    print("곱셈 연산 결과")
    print((int(firstNum)*int(secondNum)))
elif operator == '/': # 나누기라면
    print("나누기 연산 결과")
    print((int(firstNum)/int(secondNum)))
elif operator == '%': # 나머지 연산이라면
    print("나머지 연산 결과")
    print((int(firstNum)%int(secondNum)))
elif operator == '//': # 몫 계산이라면
    print("몫 연산 결과")
    print((int(firstNum)//int(secondNum)))