import random

lotto = random.sample(range(1,46),6)
# print("확인로또>> : ",lotto)
myNum = []
for i in range(6):
    no = int(input("숫자입력 : "))
    myNum.append(no)

count = 0
answer = []
for i in myNum:
    if i in lotto:
        count = count + 1
        answer.append(i)

print("로또번호 : ",lotto)
print("입력번호 : ",myNum)
print("정답번호 : ",answer)
print("정답개수 : ",count)



1.학생성적 프로그램
2.로또 맞추기
3.숫자 맞추기
