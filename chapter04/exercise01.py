# 문구 전체 개수를 담기 위한 total 변수를 정의한다
total = 0

myStationry = {}
myStationry["지우개"] = 5
myStationry["연필"] = 10
myStationry["색연필"] = 20
myStationry["공책"] = 10
myStationry["필통"] = 2
print(myStationry)
print(myStationry.keys())
print(myStationry.values())

# 지우개 1개를 다 썼다.
myStationry["지우개"] = myStationry["지우개"] - 1
print(myStationry["지우개"])

# total 출력
total = myStationry["지우개"] + myStationry["연필"] + myStationry["색연필"] + myStationry["공책"] + myStationry["필통"]
print("total : ", total)

# 연필 2자루를 잃어버렸다
myStationry["연필"] = myStationry["연필"] - 2
print(myStationry["연필"])

# total 출력
total = myStationry["지우개"] + myStationry["연필"] + myStationry["색연필"] + myStationry["공책"] + myStationry["필통"]
print("total : ", total)

# 공책 2권을 선물 받았다.
myStationry["공책"] = myStationry["공책"] + 2
print(myStationry["공책"])

# total 출력
total = myStationry["지우개"] + myStationry["연필"] + myStationry["색연필"] + myStationry["공책"] + myStationry["필통"]
print("total : ", total)