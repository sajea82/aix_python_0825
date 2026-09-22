from student import Student
from students import Students

# Students 객체선언
stus = Students() # stuList = [] 대체
#-------------삭제------------------------------------
# stuList = []
# title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
# s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1  #전역변수

# 학생성적 파일불러오기
def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline()  #1,홍길동,100,100,100,300,100.0
            if str == "": break
            # 문자열분리 리스트형태로 변경
            stu = str.split(",")
            # 타입변환
            for i,s in enumerate(stu):
                if 0<=i<=1: continue
                elif 2<=i<=5: stu[i] = int(s.strip())
                elif i==6: stu[i] = float(s.strip())
                elif i==7: stu[i] = int(s.strip())
            # Student(1,"홍길동",100,100,100)
            # 클래스 추가
            # 객체선언후 > Studens 리스트에 추가
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))
            # 번호추가부분
            stuNum = len(stus.slist)+1


            #---------삭제-----------------------------
            # stuList.append(dict(zip(s_title,stu)))
            # stuNum = len(stuList)+1

# 학생성적파일 저장하기 - stuList의 모든것을 저장시킴
def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stus.slist:
            str = s.s_str() # Student객체의 s_str()함수호출
            # str = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
            f.write(str+"\n")
        print("성적파일이 저장되었습니다.")
        print()



# 0.메인화면함수 선언
def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("9. 성적파일저장")
    print("0. 프로그램종료")
    print("-"*60)
    choice = int(input("원하는 번호 입력 : "))
    return choice

# 1. 학생성적입력함수 선언 - 클래스변경 완료
def stu_input():
    global stuNum
    while True:
        print()
        print("[ 학생성적입력 ]")
        no = stuNum
        name = input(f"{stuNum}번째. 학생이름(0.이전페이지 이동) : ")
        if name == "0": break
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        math = int(input("수학 : "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        stus.add(Student(no,name,kor,eng,math))
        #------------------삭제---------------------------
        # stuList.append({'no':no,'name':name,'kor':kor,\
        #                 'eng':eng,'math':math,\
        #                     'total':total,'avg':avg,\
        #                         'rank':rank,})
        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()
        stuNum += 1

# 2. 학생성적출력함수 선언 - 클래스변경 완료
def stu_output():
    # Students print()함수 호출
    stus.print()

    #------삭제---------------------------------------
    # print()
    # print(" "*25,end="")
    # print("[ 학생성적출력 ]")
    # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    # print("-"*60)
    # for s in stuList:
    #     print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
    # print()
# 3. 학생성적수정
def stu_update():
    print() # stus.slist
    print("[ 학생성적수정 ]")
    name = input("학생이름 검색 : ")
    temp = 0   # 임시변수
    for s in stus.slist:
        if s.name == name:
            print(f"{name}학생이 검색되었습니다.")
            print("[ 수정과목 ]")
            print("1. 국어 2. 영어 3. 수학")
            print("-"*60)
            choice = int(input("과목을 선택하세요.(0.취소)>> "))
            if choice == 0:
                break
            elif choice == 1:
                print("[ 국어점수 변경 ]")
                print("현재점수 : ",s.kor)
                s.kor = int(input("변경점수입력 :"))
        
            elif choice == 2:
                print("[ 영어점수 변경 ]")
                print("현재점수 : ",s.eng)
                s.eng = int(input("변경점수입력 :"))
    
            elif choice == 3:
                print("[ 수학점수 변경 ]")
                print("현재점수 : ",s.math)
                s.math = int(input("변경점수입력 :"))
            s.s_total()
            s.s_avg()
            print("수정이 완료되었습니다.")
            print()
    if temp==0:
        print(f"{name}학생이 없습니다. 다시 검색하세요.")

