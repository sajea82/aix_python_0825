# 학생성적 리스트
stuList = []

# 제목
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

# 딕셔너리의 key
s_title = ["no", "name", "kor", "eng", "math", "total", "avg", "rank"]

# 학생번호
stuNum = 1


# 학생성적 파일 불러오기
def readStu():
    global stuNum

    with open("c:/aaa/stu.txt", "r", encoding="utf-8") as f:
        while True:
            str = f.readline()

            if str == "":
                break

            # 문자열을 , 기준으로 분리
            stu = str.split(",")

            # 타입 변환
            for i, s in enumerate(stu):
                if 0 <= i <= 1:
                    continue
                elif 2 <= i <= 5:
                    stu[i] = int(s.strip())
                elif i == 6:
                    stu[i] = float(s.strip())
                elif i == 7:
                    stu[i] = int(s.strip())

            # 딕셔너리 생성 후 리스트에 추가
            stuList.append(dict(zip(s_title, stu)))

            # 다음 학생 번호
            stuNum = len(stuList) + 1


# 학생성적 파일 저장
def writeStu():
    with open("c:/aaa/stu.txt", "w", encoding="utf-8") as f:

        for s in stuList:
            str = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"

            f.write(str + "\n")

        print("성적파일이 저장되었습니다.")
        print()


# 0. 메인화면
def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("8. 등수처리")
    print("9. 성적파일저장")
    print("0. 프로그램종료")
    print("-" * 60)

    choice = int(input("원하는 번호 입력 : "))

    return choice


# 1. 학생성적 입력
def stu_input():
    global stuNum

    while True:
        print()
        print("[ 학생성적입력 ]")

        no = stuNum

        name = input(
            f"{stuNum}번째. 학생이름(0.이전페이지 이동) : "
        )

        if name == "0":
            break

        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        math = int(input("수학 : "))

        total = kor + eng + math
        avg = total / 3
        rank = 0

        # 딕셔너리 생성
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

        # 리스트에 추가
        stuList.append(stu)

        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()

        stuNum += 1


# 2. 학생성적 출력
def stu_output():
    print()
    print(" " * 25, end="")
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
            f"{s['no']}\t"
            f"{s['name']}\t"
            f"{s['kor']}\t"
            f"{s['eng']}\t"
            f"{s['math']}\t"
            f"{s['total']}\t"
            f"{s['avg']:.2f}\t"
            f"{s['rank']}"
        )

    print()


# 3. 학생성적 수정
def stu_update():
    print()
    print("[ 학생성적수정 ]")

    name = input("학생이름 검색 : ")

    temp = 0

    for s in stuList:

        if s["name"] == name:

            temp = 1

            print(f"{name}학생이 검색되었습니다.")

            print("[ 수정과목 ]")
            print("1. 국어 2. 영어 3. 수학")
            print("-" * 60)

            choice = int(
                input("과목을 선택하세요.(0.취소)>> ")
            )

            if choice == 0:
                break

            elif choice == 1:
                print("[ 국어점수 변경 ]")
                print("현재점수 : ", s["kor"])

                s["kor"] = int(
                    input("변경점수입력 : ")
                )

            elif choice == 2:
                print("[ 영어점수 변경 ]")
                print("현재점수 : ", s["eng"])

                s["eng"] = int(
                    input("변경점수입력 : ")
                )

            elif choice == 3:
                print("[ 수학점수 변경 ]")
                print("현재점수 : ", s["math"])

                s["math"] = int(
                    input("변경점수입력 : ")
                )

            # 합계 다시 계산
            s["total"] = (
                s["kor"]
                + s["eng"]
                + s["math"]
            )

            # 평균 다시 계산
            s["avg"] = s["total"] / 3

            print("수정이 완료되었습니다.")
            print()

    if temp == 0:
        print(
            f"{name}학생이 없습니다. 다시 검색하세요."
        )


# 8. 등수처리
def stu_rank():

    # 합계가 높은 순서로 정렬
    rankList = sorted(
        stuList,
        key=lambda s: s["total"],
        reverse=True
    )

    for i in range(len(rankList)):

        if i == 0:
            rankList[i]["rank"] = 1

        elif rankList[i]["total"] == rankList[i - 1]["total"]:
            rankList[i]["rank"] = rankList[i - 1]["rank"]

        else:
            rankList[i]["rank"] = i + 1

    print("등수처리가 완료되었습니다.")
    print()


# 메인 프로그램
readStu()

while True:

    choice = main_screen()

    if choice == 1:
        stu_input()

    elif choice == 2:
        stu_output()

    elif choice == 3:
        stu_update()

    elif choice == 8:
        stu_rank()

    elif choice == 9:
        writeStu()

    else:
        print("프로그램 종료")
        break
