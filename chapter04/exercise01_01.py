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

# myStationry.values()를 이용해 문구마다 개수를 구해서 v에 넣은 후, 반복문을 통해 total에 누적시킨다.
total = 0
for v in myStationry.values(): # values() 메소드는 dict_values 타입으로, list와 비슷하게 데이터를 관리하여 사용할 수 있다.
    total += v
print('total : {0}'.format(total))


# 연필 2자루를 잃어버렸다
myStationry["연필"] = myStationry["연필"] - 2
print(myStationry["연필"])

total = 0
for v in myStationry.values():
    total += v
print('total : {0}'.format(total))


# 공책 2권을 선물 받았다.
myStationry["공책"] = myStationry["공책"] + 2
print(myStationry["공책"])

total = 0
for v in myStationry.values():
    total += v
print('total : {0}'.format(total))
