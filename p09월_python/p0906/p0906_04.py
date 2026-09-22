title = ["번호","이름","국어","영어","수학","합계","평균"]
k_title = ["no","name","kor","eng","math","total","avg"]
stu = []
sno = 1 

def s_mainPrint():
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력 ")
    print("2. 학생성적출력 ")
    print("3. 학생성적수정 ")
    print("4. 학생성적파일저장") 
    print("0. 프로그램종료 ")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>>"))
    print()
    return choice

def s_input():
    while True:
                no = sno
                print("[ 학생성적입력 ]")
                name = input(f"{no}번째 학생이름입력(0.이전화면이동): ")
                if name == "0": break
                kor = int(input("국어성적입력 : "))
                eng = int(input("영어성적입력 : "))
                math = int(input("수학성적입력 : "))
                total = kor + eng + math
                avg = total/3
                stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
                print(f"{name}학생정보가 저장되었습니다.")
                print()
                sno += 1
                s_output()

def s_output():
    print()
    print("[ 학생정보출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    if len(stu) ==0:
        print("**학생정보가 데이터에 없습니다.**")
    else:
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            print()

def s_update():
    print()
    print("[ 학생성적수정 ]")
    name = input("찾으려는 학생을 입력하세요>> ")
    temp = 0
    for i,s in enumerate(stu):
        if s["name"] == name:
            print(f"{name} 학생을 찾았습니다.")
            temp = 1

            print("[ 과목선택 ]")
            print("1. 국어 2. 영어 3. 수학")
            choice = int(input("원하는 과목을 선택하세요.>> "))

            print(f"현재{title[choice+1]}점수 : {s[k_title[choice+1]]}")
            s[k_title[choice+1]] = int(input(f"변경하려는{title[choice+1]}점수입력:"))
            s[title] = s["kor"] + s["eng"] +s["math"]
            s[avg] = s[title]/3
            print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]}점수가 변경되었습니다.")
            break
    if temp ==0:
        print(f"{name}학생이 없습니다.")

# 메인화면
while True:
    choice = s_mainPrint()
    # 학생성적입력
    if choice == 1:
        s_input()
    # 학생성적출력
    if choice == 2:
        s_output()
    # 학생성적수정
    if choice == 3:
        s_update()


