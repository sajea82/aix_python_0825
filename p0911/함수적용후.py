total = ["번호","이름","국어","영어","수학","합계","평균"]
k_total = ["no","name","kor","eng","math","total","avg"]
stuList =[]
stuNum = 1

def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력 ")
    print("2. 성적출력 ")
    print("3. 성적수정 ")
    print("9. 성적파일저장 ")
    print("0. 프로그램종료 ")
    print("-"*60)
    choice = int(input("원하는 번호입력하세요.>>"))
    return choice

def stu_input():
    global stuList
    while True:
        no = len(stuList) + 1
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 학생이름입력(0. 이전화면이동):")
        if name == "0": break
        kor = int(input("국어성적입력 : "))
        eng = int(input("영어성적입력 : "))
        math = int(input("수학성적입력 : "))
        total = kor + eng + math
        avg = total/3
        stuList.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
        print(f"{name}학생이 저장되었습니다.")
        print()

def stu_output():
    print()
    print("[ 학생성적출력 ]")
    print("-"*60)
    print(f"{'번호'}\t{'이름'}\t{'국어'}\t{'영어'}\t{'수학'}\t{'합계'}\t{'평균'}")
    print("-"*60)
    for s in stuList:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
        print()

def stu_update():
    print()
    print("[ 학생성적수정 ]")
    name = input("학생이름검색 : ")
    temp = 0
    for s in stuList:
        if s['name'] == name:
            temp = 1
            print(f"{name}학생이 검색되었습니다.")
            print("[ 수정과목선택 ]")
            print("1. 국어 2. 영어 3. 수학")   
            print("-"*60)
            choice = int(input("과목선택(0. 취소): "))  
            if choice == 0: break
            elif choice == 1:
                print("[ 국어점수 변경 ]")
                print("현재점수 : ",s['kor'])
                s['kor'] = int(input("변경점수입력 :"))
            elif choice == 2:
                print("[ 영어점수 변경 ]")
                print("현재점수 : ",s['eng'])
                s['eng'] = int(input("변경점수입력 :"))
            elif choice == 3:
                print("[ 수학점수 변경 ]")
                print("현재점수 : ",s['math'])
                s['math'] = int(input("변경점수입력 :"))

            s['total'] = s['kor'] + s['eng'] + s['math']
            s['avg'] = s['total']/3        
            print("수정이 완료되었습니다.")
            print()
        if temp == 0:
            print(f"{name}학생이 없습니다. 다시 검색하세요.")

def writeStu():
    global stuList
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
                for s in stuList:
                    date = f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\n"
                    f.write(date)
    
                print("성적파일이 저장되었습니다.")
                print()

while True:
    choice = main_screen()

    if choice == 1:
        stu_input()

    elif choice == 2:
        stu_output()

    elif choice == 3:
        stu_update()

    elif choice == 9:
        writeStu()
    else:
        print("[ 프로그램종료 ]") 
        print 