# 숫자가 저장된 변수 2개를 만들고 각각의 변수를 이용해서 사칙연산을 시켜보자.
import random

ranNum = random.sample(range(1,100),2)

testNum1 = ranNum[0]
testNum2 = ranNum[1]

print("testNum1 = ", testNum1)
print("testNum2 = ", testNum2)

print("testNum1 + testNum2 = ", testNum1 + testNum2)
print("testNum1 - testNum2 = ", testNum1 - testNum2)
print("testNum1 * testNum2 = ", testNum1 * testNum2)
print("testNum1 / testNum2 = ", testNum1 / testNum2)