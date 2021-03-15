myStationry = {}
myStationry["지우개"] = 5
myStationry["연필"] = 10
myStationry["색연필"] = 20
myStationry["공책"] = 10
myStationry["필통"] = 2

print(myStationry)
print(myStationry.keys())
print(myStationry.values())

# 지우개를 1개 다 썼다.
myStationry["지우개"] = myStationry["지우개"] - 1
print(myStationry["지우개"])

# 연필 2자루를 잃어버렸다.
myStationry["연필"] = myStationry["연필"] - 2
print(myStationry["연필"])

# 공책 2권을 선물 받았다.
myStationry["공책"] = myStationry["공책"] + 2
print(myStationry["공책"])

