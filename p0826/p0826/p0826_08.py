# # 번호,이름,국어,영어,수학을 입력받아
# # 번호,이름,국어,영어,수학,합계, 평균을 출력하시오.
# # 1 홍길동 100 100 100 300 100.0

# # 1 홍길동
# no = input("번호 입력>>")
# name = input("이름 >>")
# kor = int(input("국어점수 입력>>"))
# eng = int(input("영어점수 입력>>"))
# math = int(input("수학점수 입력>>"))
# total = kor+eng+math
# avg = total/3



# # 2 유관순 100 100 91
# no2 = input("번호 입력>> ")
# name2 = input("이름 입력>> ")
# kor2 = int(input("국어점수 입력>> "))
# eng2 = int(input("영어점수 입력>> "))
# math2 = int(input("수학점수 입력>> "))
# total2 = kor+eng+math
# avg2 = total2/3

# print("-"*60)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,total,avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no2,name2,kor2,eng2,math2,total2,avg2))
# print("-"*60)

# 1 김철수 100 100 100
# no = input("번호 입력>>")
# name = input("이름 입력>>")
# kor = int(input("국어점수 입력>>"))
# eng = int(input("영어점수 입력>>"))
# math = int(input("수학점수 입력>>"))
# total = kor+eng+math
# avg = total/3
# print("-"*60)
# print("번호\t이름\t 국어\t 영어\t 수학\t 합계\t 평균")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,total,avg))
# print("-"*60)

# 1 박영훈 100 80 75 90
no = input("번호 입력>>")
name = input("이름 입력>>")
kor = int(input("국어점수 입력>>"))
eng = int(input("영어점수 입력>>"))
math = int(input("수학점수 입력>>"))
sci = int(input("과학점수 입력>>"))
total = kor+eng+math+sci
avg = total/4
print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t과학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no,name,kor,eng,math,sci,total,avg))
print("-"*60)








