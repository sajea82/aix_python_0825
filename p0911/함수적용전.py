stuList = []

# 학생 1명 입력
no = 1
name = input("학생이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

total = kor + eng + math
avg = total / 3
rank = 0

# 딕셔너리로 학생 정보 저장
stu = {
    "no": no,
    "name": name,
    "kor": kor,
    "eng": eng,
    "math": math,
    "total": total,
    "avg": avg,
    "rank": rank
}

stuList.append(stu)

# 학생성적 출력
print()
print("[ 학생성적출력 ]")
print("-" * 60)

print(
    "번호",
    "이름",
    "국어",
    "영어",
    "수학",
    "합계",
    "평균",
    "등수",
    sep="\t"
)

print("-" * 60)

for s in stuList:
    print(
        s["no"],
        s["name"],
        s["kor"],
        s["eng"],
        s["math"],
        s["total"],
        f"{s['avg']:.2f}",
        s["rank"],
        sep="\t"
    )
