# # 1.홍길동, 100,100,100,300,100.0
# # 2.유관순, 100,100,100,300,100.0 

# no = input("번호입력>> ")
# name = input("이름 입력 : ")
# kor = int(input("국어성적입력 : "))
# eng = int(input("영어성적입력 : "))
# math = int(input("수학성적입력 : "))
# total = kor + eng + math
# avg = total/3

# no2 = input("번호입력>> ")
# name2 = input("이름 입력>> ")
# kor2 = int(input("국어성적입력 : "))
# eng2 = int(input("영어성적입력 : "))
# math2 = int(input("수학성적입력 : "))
# total2 = kor2 + eng2 + math2
# avg2 = total2/3

# print("-"*60)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no,name,kor,eng,math,total,avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no2,name2,kor2,eng2,math2,total2,avg2))
# print("-"*60)

# stu = []
# c_no = 1
# # 학생성적프로그램 메인부분
# while True:
#     print("[ 학생성적프로그램 ]")
#     print("1. 학생성적입력 ")
#     print("2. 학생성적출력 ")
#     print("3. 학생성적수정 ")
#     print("4. 학생성적삭제 ")
#     print("0. 프로그램종료 ")
#     print("-"*60)
#     choice = int(input("원하는 번호를 입력하세요.>> "))
#     print()

#     if choice == 1:
#         while True:
#             no = c_no
#             print("[ 학생성적입력 ]")
#             name = input("학생이름 입력(이전페이지 : 0): ")
#             if name =="0": break
#             kor = int(input("국어성적입력: "))
#             eng = int(input("영어성적입력: "))
#             math = int(input("수학성적입력: "))
#             total = kor + eng + math
#             avg = total/3
#             stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
#             print("학생성적이 입력되었습니다.")
#             c_no +=1
#         print()
        
#     if choice == 2:
#             print("[ 학생성적출력 ]")
#             print("-"*60)
#             print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
#             print("-"*60)
#             for s in stu:
#                 print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\
# \t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
                # print()

#---------------------------------------------------------------------------------------------------

stu = []
c_no = 1
# 메인입력
while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력 ")
    print("2. 학생성적출력 ")
    print("3. 학생성적수정 ")
    print("4. 학생성적삭제 ")
    print("0. 프로그램종료 ")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>> "))
# 학생성적입력
    if choice == 1:
        while True:
            print("[ 학생성적입력 ]")
            no = c_no
            name = input("학생이름입력 (이전페이지 : 0): ")
            if name =="0": break
            kor = int(input("국어성적입력 : "))
            eng = int(input("영어성적입력 : "))
            math = int(input("수학성적입력 : "))
            total = kor + eng + math
            avg = total/3
            stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
            c_no += 1
            print("학생성적이 등록되었습니다.")
            print()
# 학생성적출력
    if choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\
\t{s['total']}\t{s['avg']}:.2f")
            print()
















