# 학생2명의 성적을 출력하시오.
# 번호,이름,국어,영어,수학 점수를 입력받아
# 번호,이름,국어,영어,수학,합계,평균을 출력하시오.

# 1.성적입력
# 2.성적처리 수식
# 3.성적출력
# no = input("번호입력 :")
# name = input("이름입력 :")

# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")


# 1 김아이 100 90 40
# 1. 성적입력
no = input("번호입력 : ")
name = input("이름입력 : ")
kor = int(input("국어성적 입력 : ")) # 한줄복사 shirt+alt+방향키
eng = int(input("영어성적 입력 : "))
math = int(input("수학성적 입력 : "))
# 2.성적처리 수식
total = kor+eng+math
avg = total/3
# 3. 성적출력
print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t,{}\t,{}\t,{}\t,{}\t,{}\t,{:.2f}".\
      format(no,name,kor,eng,math,total,avg))
print("-"*60)




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
