firstNum = input()
operator = input()
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