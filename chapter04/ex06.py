# 딕셔너리(Dictionary) : java의 map과 비슷하게 key:value의 한쌍으로 이루어진 list이다.
# 중괄호를 사용하여 만든다. json과 비슷하게 나오는듯

# 데이터 추가
# 딕셔너리 생성
# 데이터가 없는 비어있는 딕셔너리 생성
dicVar2 = {}
# 키와 밸류를 가지고 5개의 데이터를 집어넣는다
dicVar2["정우람"] = 30
dicVar2["박으뜸"] = 26
dicVar2["배힘찬"] = 31
dicVar2["천영웅"] = 28
dicVar2["신석기"] = 25
# 딕셔너리의 전체 데이터 출력
print(dicVar2)

# 데이터 참조 및 수정하기
# 키가 천영웅에 해당하는 데이터 출력하기
print(dicVar2["천영웅"])
# 키가 배힘찬에 해당하는 데이터 출력하기
print(dicVar2["배힘찬"])
# 키가 신석기에 해당하는 데이터 출력하기
print(dicVar2["신석기"])

# 키가 천영웅에 해당하는 데이터를 31로 수정한다
dicVar2["천영웅"] = 31
print(dicVar2["천영웅"])
# 키가 배힘찬에 해당하는 데이터를 31로 수정한다
dicVar2["배힘찬"] = 32
print(dicVar2["배힘찬"])
# 키가 신석기에 해당하는 데이터를 31로 수정한다
dicVar2["신석기"] = 26
print(dicVar2["신석기"])

# 데이터 삭제하기
# 데이터 삭제 전 dicVar2의 전체 데이터를 출력한다
print(dicVar2)
# dicVar2에서 키 값이 '정우람'인 데이터를 del키워드를 이용해서 삭제한다.
del dicVar2['정우람']
# 데이터 삭제 후 dicVar2의 전체 데이터를 출력한다
print(dicVar2)

# 데이터 갯수 확인
# len 함수를 이용하면 데이터 갯수를 확인 할 수 있다.
print(len(dicVar2))
