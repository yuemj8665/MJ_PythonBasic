# 시나리오 1 : 학급 학생 수가 10명인 리스트를 만든다.
students = ["정우람","박으뜸","배힘찬","천영웅","신석기","배민규","전민수","박건우","박찬호","이승엽"]
print(students)

# 시나리오 2 : '가나다' 순으로 정렬한다
students.sort()
print(students)

# 시나리오 3 : '박찬호' 학생의 전학으로 학급에서 제하고 전체 학생 수를 나타내자.
students.remove("박찬호")
print(students)
print(len(students))

# 시나리오 4 : 선생님을 돕기위해 앞에서 3명의 학생을 뽑는다.
print(students[:3])

# 시나리오 5 : 새로운 친구가 전학왔다. (이름 : 정민규)
students.append("정민규")
students.sort()
print(students)

# 시나리오 6 : 자리를 바꾸기 위해서 학생을 역순으로 변경
students.sort(reverse=True)
print()

# 시나리오 7 : 정우람 학생이 정미남으로 이름을 개명했다.
indexStudent = students.index("정우람")
students[indexStudent] = "정미남"
print(students)