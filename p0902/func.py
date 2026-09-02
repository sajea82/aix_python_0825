import random

def ran_number(choice):
    if choice == 1:
    # 랜덤숫자 5개
        result = random.sample(range(1,100),5)
    elif choice == 2:
    # 랜덤숫자 3개
        result = random.sample(range(1,100),3)
    else:
    # 랜덤숫자 1개
        result = random.sample(range(1,100),1)
    return result

def main_print():
# 1-100번사이 숫자
    print("1. 랜덤숫자 5개 가져오기")
    print("2. 랜덤숫자 3개 가져오기")
    print("3. 랜덤숫자 1개 가져오기")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice

# # 프로그램 시작--->
# while True:
#     choice = main_print()
#     result = ran_number(choice)
#     print("결과 : ",result)
