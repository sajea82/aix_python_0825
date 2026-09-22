# 1-100사이의 랜덤번호를 맞추는 프로그램을 구현하시오
# 랜덤번호보다 높은 수를 입력하면 낮은 숫자입력!! 높은 숫자입력!!
# 정답을 맞추면
# 정답숫자 :
# 숫자입력회수 :
# 입력한숫자 :

import random
random = random.randint(1,101)
my_list = []
myNum = 0
answer = 0
while True:
    myNum = int(input("1-100사이 숫자를 입력 : "))
    my_list.append(myNum)

    if myNum == random:
        answer = myNum
        print("정답입니다.")
        break
    elif myNum>random:
        print("입력한 숫자보다 높으면 낮은 숫자 입력!!")
    else:
        print("입력한 숫자보다 낮으면 높은 숫자 입력!!")


print("정답 : ",answer)
print("정답 : ",my_list)
print("입력한 모든 숫자 : ",my_list)

print("프로그램 종료")




