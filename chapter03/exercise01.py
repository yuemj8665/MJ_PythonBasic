# 파이썬 위키피디아 검색 결과를 변수에 할당한다.
py = 'Python is an interpreted, high-level and general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[29]  Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a \"batteries included\" language due to its comprehensive standard library.[30]  Guido van Rossum began working on Python in the late 1980\'s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.1.[31] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[32] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.  Python consistently ranks as one of the most popular programming languages.[33][34][35][36]'
# 절취선
line = "====================================="

# 1. Guido van Rossum의 인덱스 찾기
# 2. Python이 몇번 등장하는지
# 3. Python단어를 파이썬으로 변경하기
# 4. ' ' 문자를(공백) 활용하여 List타입으로 변경하기
# 5. 모든 문자를 소문자로 변경하기
# 6. 모든 문자를 대문자로 변경하기

##################################################################################
# 1. Guido van Rossum의 인덱스 찾기
print(line)
print("1. Guido van Rossum의 인덱스 찾기")
print(line)
print(py.find('Guido van Rossum'))
print()
print(line)
# 2. Python이 몇번 등장하는지
print("2. Python이 몇번 등장하는지")
print(line)
print(py.count('Python'))
print()
print(line)
# 3. Python단어를 파이썬으로 변경하기
print("3. Python단어를 파이썬으로 변경하기")
print(line)
print(py.replace('Python','파이썬'))
print()
print(line)
# 4. ' ' 문자를(공백) 활용하여 List타입으로 변경하기
print("4. ' ' 문자를(공백) 활용하여 List타입으로 변경하기")
print(line)
pyList = py.split(' ')
print(pyList)
print(len(pyList))
print()
print(line)
# 5. 모든 문자를 소문자로 변경하기
print(line)
print('5. 모든 문자를 소문자로 변경하기')
print(py.lower())
print()
print(line)
# 6. 모든 문자를 대문자로 변경하기
print('6. 모든 문자를 대문자로 변경하기')
print(line)
print(py.upper())
##################################################################################