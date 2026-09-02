# 1. 박영훈 100 50 70 
no = input("번호입력 :")
name = input("이름입력 :")
kor = int(input("국어성적 입력 :"))
eng = int(input("영어성적 입력 :"))
math = int(input("수학성적 입력 :"))
total = kor+eng+math
avg = total/3

# 2. 이경화 100 70 20 
no2 = input("번호입력 :")
name2 = input("이름입력 :")
kor2 = int(input("국어성적 입력 :"))
eng2 = int(input("영어성적 입력 :"))
math2 = int(input("수학성적 입력 :"))
total2 = kor2+eng2+math2
avg2 = total2/3

# 3. 박현준 100 50 40 
no3 = input("번호입력 :")
name3 = input("이름입력 :")
kor3 = int(input("국어점수 입력 :"))
eng3 = int(input("영어점수 입력 :"))
math3 = int(input("수학점수 입력 :"))
total3 = kor3+eng3+math3
avg3 = total3/3

print("-"*60)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
    format(no,name,kor,eng,math,total,avg))
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
      format(no2,name2,kor2,eng2,math2,total2,avg2))
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
      format(no3,name3,kor3,eng3,math3,total3,avg3))
print("-"*60)


