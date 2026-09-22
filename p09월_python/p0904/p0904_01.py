# title = ["번호","이름","국어","영어","수학","합계","평균"]
# k_title = ["no","name","kor","eng","math","total","avg"]
# stu = []
# sno = 1  # 학생성적인원변수 - db

stu = []
sno = 1

while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력 ")
    print("2. 학생성적출력 ")
    print("3. 학생성적수정 ")
    print("-"*60)
    print()
    choice = int(input("원하는 입력번호를 누르세요.>> "))
    print()
    if choice == 1:
        while True:
            no = sno
            print("[ 학생성적입력 ]")
            name = input("학생이름입력:")
            kor = int(input("국어점수입력 : "))
            eng = int(input("영어점수입력 : "))
            math = int(input("수학점수입력 : "))
            total = kor + eng + math
            avg = total/3  
            stu.append([no,name,kor,eng,math,total,avg])  
            print("학생성적이 등록되었습니다.")
            print()
    if choice == 2:
        print()
        print("[ 학생성적출력 ]")
        print("입력된 학생성적 : ",len(stu))
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print("")









