tital = ["번호","이름","국어","영어","수학","합계","평균"]
k_tital = ["no","name","kor","eng","math","total","avg"]
stu = []
sno = 1

def s_mainPint():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력 ")
    print("2. 성적출력 ")
    print("3. 성적수정 ")
    print("9. 성적파일저장 ")
    print("0. 프로그램종료 ")
    print("-"*60)
    choice = int(input("원하는 번호를 입력 : "))
    return choice

def s_input():
    global sno
    while True:
        no = sno
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 이름입력(0. 이전화면이동):")
        if name =="0": break
        kor = int(input("국어성적입력 : "))
        eng = int(input("영어성적입력 : "))
        math = int(input("수학성적입력 : "))
        total = kor + eng + math
        avg = total/3
        stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
        print()
        sno +=1
    
def s_output():
    print()
    print("[ 학생성적출력 ]")     
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*tital))
    print("-"*60)
    if len(stu) ==0:
        print("**학생 데이터가 없습니다.**")
    else:
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}")
            print()

def s_update():
    print()
    print("[ 학생성적수정 ]")
    name = input("찾으려는 학생이름 입력: ")
    temp = 0
    for i,s in enumerate(stu):
        if s["name"] == name:
            print(f"{name}학생을 찾았습니다.")
            temp = 1

            print("[ 과목선택 ]")
            print("1. 국어 2. 영어 3. 수학")
            choice = int(input("원하는 과목선택: "))

            print(f"현재{[tital[choice+1]]}점수 : {s[k_tital[choice+1]]}")
            s[k_tital[choice+1]] = int(input(f"변경하려는{tital[choice+1]}점수입력:"))
            s["total"] = s["kor"] + s["eng"] + s["math"]
            s["avg"] = s["total"]/3
            print(f"{s[k_tital[choice+1]]}점으로 {tital[choice+1]} 변경하였습니다.")
            print()
            break
    if temp == 0:
        print(f"{name}학생을 찾을수가 없습니다.")

def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stu:
            data = (f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
            f.write(data + "\n")
            print("성적파일이 저장되었습니다.")
            print() 

while True:
    choice = s_mainPint()
    if choice == 1:
        s_input()
    elif choice == 2:
        s_output()
    elif choice == 3:
        s_update()
    elif choice == 9:
        writeStu()
    elif choice == 0:
        print("프로그램종료")
        break
    else:
        print("번호를 잘못 입력했습니다.")







