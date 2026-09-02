# 학생 성적표
# 준비단계
name = []
kor = []
eng = []
math = []
total = []
avg = []

# 입력
for i in range(3):
    name.append(input("이름입력 : "))
    k_input = int(input("국어점수 : "))
    kor.append(k_input)
    e_input = int(input("영어점수 : "))
    eng.append(e_input)
    m_inlput = int(input("수학점수 : "))
    math.append(m_inlput)
# 처리
    total.append(k_input + e_input + m_inlput)
    avg.append((k_input + e_input + m_inlput)/3)

# 결과
print("[학생성적표]")
print("이름\t국어\t영어\t수학\t합계\t평균") 
print("-"*60)   
for i in range(len(name)):
    print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
      t{total[i]}\t{avg[i]:.2f}")