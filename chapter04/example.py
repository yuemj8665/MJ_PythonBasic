# 문구 관리 대장 만들기
# myStaionery 변수를 만들고 중괄호를 이용해서 딕셔너리 컨테이너로 초기화한다
myStaionery = {}

myStaionery["지우개"] = 5
myStaionery["연필"] = 10
myStaionery["색연필"] = 20
myStaionery["공책"] = 10
myStaionery["필통"] = 2
print(myStaionery)

# keys() 메소드를 사용하면 key 값들만 얻을 수 있다.
print(myStaionery.keys())
# values() 메소드를 사용하면 value 값들만 얻을 수 있다.
print(myStaionery.values())

# 시나리오 1 : 지우개 1개를 다 썼다
myStaionery["지우개"] = myStaionery["지우개"] - 1
print(myStaionery["지우개"])

# 시나리오 2 : 연필 2자루를 잃어버렸다
myStaionery["연필"] = myStaionery["연필"] - 2
print(myStaionery["연필"])

# 시나리오 3 : 공책 2권을 선물 받았다.
myStaionery["공책"] = myStaionery["공책"] + 2
print(myStaionery["공책"])