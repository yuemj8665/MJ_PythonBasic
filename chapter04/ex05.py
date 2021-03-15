# 튜플
# 튜플은 리스트와 비슷하지만 데이터를 변경할 수 없다. class1 = ("a","b","c")....

# 길이가 3인 class1 튜플을 만든다.
class1 = ("정우람","박으뜸","배힘찬")

# class1 전체 출력
print(class1)

# 인덱스를 이용해서 데이터를 참조한다.
print(class1[0])
print(class1[1])
print(class1[2])

# 튜플 길이 확인하기
# 리스트와 마찬가지로 len() 함수를 사용한다.
length = len(class1)
# 튜플의 길이 출력
print(length)

# 튜플 결합하기
# 새로운 class2 튜플을 생성한다
class2 = ("박찬호","이승엽","이병규")
# class1과 class2를 + 연산자를 사용하여 결합하고 classSum에 담는다.
classSum = class1 + class2
# classSum의 데이터 타입을 확인한다. classSum은 Tuple타입이다.
print(type(classSum))
# classSum을 출력해서 튜플이 정상 결합된것을 확인한다.
print(classSum)

# 튜플 데이터 슬라이싱
# 데이터 슬라이싱
print(classSum)
# 인덱스 0부터 3앞까지
print(classSum[:3])
# 인덱스 1부터 3앞까지
print(classSum[1:3])
# 인덱스 3부터 끝까지
print(classSum[len(classSum)-3:])

# 특정 데이터의 인덱스 찾기
# index() 메서드
# "박찬호" 데이터의 인덱스 값을 index() 메서드를 사용하여 찾는다.
indexNum = classSum.index("박찬호")
# 반환받은 타입 확인
print(type(indexNum))
# 반환된 인덱스 값 출력
print(indexNum)

# 특정 데이터 갯수 찾기
# count() 메서드
# 중복 데이터가 포함된 튜플을 찾는다.
class3 = ("정우람","박으뜸","배힘찬","정우람","이승엽","배힘찬")
# 튜플 전체를 출력한다.
print(class3)
# count() 메소드를 사용해 정우람이 몇갠지 확인한다
num = class3.count("정우람")
print(num)
# count() 메소드를 사용해 박으뜸이 몇갠지 확인한다
num = class3.count("박으뜸")
print(num)
# count() 메소드를 사용해 배힘찬이 몇갠지 확인한다
num = class3.count("배힘찬")
print(num)
