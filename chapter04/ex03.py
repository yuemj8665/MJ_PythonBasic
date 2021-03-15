# list => java에서의 list와 똑같다.
# 리스트를 선언하고 초기화 한다.
listVar1 = [123,3.14,"파이썬"]

# 리스트의 전체 데이터를 출력한다
print("# 리스트의 전체 데이터를 출력한다")
print(listVar1)

# 각 인덱스에 해당하는 데이터 출력
print("# 각 인덱스에 해당하는 데이터 출력")
print(listVar1[0])
print(listVar1[1])
print(listVar1[2])

# 데이터 추가
# append() 함수를 사용하여 listVar1 리스트에 "python" 요소를 추가한다.
print("# append() 함수를 사용하여 listVar1 리스트에 \"python\" 요소를 추가한다.")
listVar1.append("python")

# 리스트의 전체 데이터 출력으로 추가된 요소 확인하기
print("# 리스트의 전체 데이터 출력으로 추가된 요소 확인하기")
print(listVar1)

# 데이터 삭제
# 리스트에서 마지막 데이터를 삭제한다.
listVar1.pop()

# 리스트의 전체 데이터 출력으로 삭제된 요소 확인하기
print("# 리스트의 전체 데이터 출력으로 삭제된 요소 확인하기")
print(listVar1)

# 특정 인덱스 삭제
# 인덱스가 1인 데이터를 삭제한다.
listVar1.pop(1)

# 리스트의 전체 데이터 출력으로 삭제된 요소 확인하기
print("# 리스트의 전체 데이터 출력으로 삭제된 요소 확인하기")
print(listVar1)

# 갑자기 궁금해졌는데 삭제 한 인덱스는 빈공간을 채우는가? 결과는 YES 다.
print(listVar1[1])

# 리스트 길이 확인하기
# len() 함수를 이용하여 listVar1의 리스트 길이를 출력한다.
print("# len() 함수를 이용하여 listVar1의 리스트 길이를 출력한다.")
print(len(listVar1))

# 리스트 연장
# 새로운 listVar2 생성
listVar2 = ["c", "c++", "java"]

#listVar1에 extend() 함수를 이용하여 listVar2 리스트를 붙여 연장한다.
listVar1.extend(listVar2)

# 데이터가 연장된 listVar1 리스트를 출력한다.
print("# 데이터가 연장된 listVar1 리스트를 출력한다.")
print(listVar1)

# 특정 위치에 데이터 삽입하기
# insert() 함수를 이용해서 인덱스 2에 program 문자열을 추가한다.
listVar1.insert(2,"program")

# 데이터가 추가된 listVar1 리스트를 출력한다.
print("# 데이터가 추가된 listVar1 리스트를 출력한다.")
print(listVar1)

# 특정 데이터 삭제
# remove() 함수를 이용해서 데이터가 "c"인 요소를 찾아 삭제한다
listVar1.remove("c")

# 데이터 "c"가 제거된 listVar1 리스트를 출력한다
print("# 데이터 \"c\"가 제거된 listVar1 리스트를 출력한다")
print(listVar1)

# remove() 함수를 이용해서 데이터가 "c++"인 요소를 찾아 삭제한다
listVar1.remove("c++")

# 데이터 "c++"가 제거된 listVar1 리스트를 출력한다
print("# 데이터 \"c++\"가 제거된 listVar1 리스트를 출력한다")
print(listVar1)

# 특저 데이터가 여러 개인 경우 삭제
listVar3 = ["c","c++","java","c","c++"]

print(listVar3)

# remove() 함수를 이용해서 리스트의 첫 번쨰 "c"만 삭제
listVar3.remove("c")

# 첫 번째 "c" 삭제 확인, 아마 인덱스 빠른 순으로 삭제하는 듯 함.
print("# 첫 번째 \"c\" 삭제 확인")
print(listVar3)

# 데이터 정렬
# 정렬하지 않은 리스트를 만든다.
listVar4 = [4,3,5,6,1,2,3,4,7,2]
print(listVar4)

# sort() 함수를 이용하여 오름차순 정렬을 한다. default로 오름차순이다.
print("# sort() 함수를 이용하여 오름차순 정렬을 한다. default로 오름차순이다.")
listVar4.sort(reverse=False)

print(listVar4)

# sort() 함수를 이용하여 내림차순 정렬을 한다.
print("# sort() 함수를 이용하여 내림차순 정렬을 한다.")
listVar4.sort(reverse=True)

print(listVar4)

# 데이터 역순으로 나타내기
# listVar 리스트를 만들기
listVar5 = ["c","c++","c#","java","python"]
print(listVar5)

# reverse() 함수를 이용하여 데이터를 반대로 뒤집는다.
listVar5.reverse()
print(listVar5)

# reverse() 함수를 이용하여 데이터를 다시 반대로 뒤집는다. 결국 다시 원상복귀
listVar5.reverse()
print(listVar5)

# 데이터 슬라이싱
# 길이가 5인 listVar6 리스트를 만든다.
listVar6 = ["호랑이","사자","곰","여우","늑대"]
print(listVar6)

# 앞에서 3개의 데이터 슬라이싱
# 맨 앞에서부터 인덱스 3 앞까지의 데이터를 슬라이스 한다.
print("# 맨 앞에서부터 인덱스 3 앞까지의 데이터를 슬라이스 한다.")
print(listVar6[:3])

# 중간에서 3개의 데이터 슬라이싱
# 인덱스 1부터 인덱스 4 앞까지의 데이터를 슬라이스 한다.
print("# 인덱스 1부터 인덱스 4 앞까지의 데이터를 슬라이스 한다.")
print(listVar6[1:4])

# 뒤에서 3개의 데이터 슬라이싱
# 인덱스 3부터 끝까지 슬라이싱 한다.(len(listVar6) -> 리스트 전체 길이(5)
print("# 인덱스 3부터 끝까지 슬라이싱 한다")
print(listVar6[len(listVar6)-2:])