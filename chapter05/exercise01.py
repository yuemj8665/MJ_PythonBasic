# 학생 5명의 수학 점수를 입력 후 평균 값이 80점 이상이라면 PASS, 아니라면 Try Again을 입력하기
total = 0
studentList = {}
print("첫 번쨰 학생의 점수를 입력하세요")
studentList[0] = int(input())
print("두 번쨰 학생의 점수를 입력하세요")
studentList[2] = int(input())
print("세 번쨰 학생의 점수를 입력하세요")
studentList[3] = int(input())
print("네 번쨰 학생의 점수를 입력하세요")
studentList[4] = int(input())
print("다섯 번쨰 학생의 점수를 입력하세요")
studentList[5] = int(input())

for score in studentList.values() :
    total += score

print("total.. : ",total)
print("평균 점수.. : ",total/len(studentList))

if total >= 80:
    print("PASS")
else :
    print("Try Again")
