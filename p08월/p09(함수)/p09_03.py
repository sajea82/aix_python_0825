my_info = {"id":"aaa","pw":"1111","money":10_000_000,"bonusPoint":0}

cart = []

product = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
]

while True:
    print("[ 쇼핑몰에 오신것을 환영합니다. ]")
    id = input("아이디 : ")
    pw = input("패스워드 : ")

    if my_info["id"] == id and my_info["pw"]==pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("아이디 또는 패스워드가 일치하지 않습니다.")

print(f"현재 보유금액 : {my_info['money']:,}원")
print(f"현재 보너스포인트 : {my_info['bonusPoint']:,}포인트")
print("-"*40)
while True:
    print()
    print("[ 쇼핑몰 구매사이트 ]")
    for i,p in enumerate(product):
        print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    if choice == 1:
        no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0) "))
        if no == 1:
            print("구매완료")
            # 계산후 결과
            my_info['money'] -= product[0]['price']
            # my_info['money'] = my_info['money'] - product[0]['price']

            my_info['bonusPoint'] += product[0]['bonusPoint']
            print(f"m머니 : {my_info['money']:,}원")
            print(f"m보너스포인트 : {my_info['bonusPoint']:,}포인트")
        else:
            print("이전화면으로 이동합니다.")
    elif choice == 2:
        pass

# -----------------------------------------------------------------

my_info = {"id":"aaa","pw":"1111","name":"홍길동","money":10000000}

s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

def p_cal(choice):
    if my_info['money']<s_arr[choice-1]['price']:
        print("보유금액이 부족합니다. 머니충전을 한후 구매하세요.")
        return
    print(f"구매상품 : {s_arr[choice-1]['prd_name']}")
    print(f"가격 : {s_arr[choice-1]['price']:,} 원")
    # 계산하는 부분
    my_info['money'] -= s_arr[choice-1]['price']
    print(f"상품구매후 보유금액 : {my_info['money']:,}원")

while True:  #{"prd_name":"컴퓨터","price":1000000}
    for i,v in enumerate(s_arr): # (0,"컴퓨터"),(1,"냉장고")
        print(f"{i+1}. {v['prd_name']} : {v['price']:,} 원")

    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:   # 컴퓨터 - 1000000
        p_cal(choice)
    elif choice == 2: # 냉장고 - 2000000
        p_cal(choice)
    elif choice == 3: # 오디오 - 500000
        p_cal(choice)
    elif choice == 4: # 세탁기 - 1500000
        p_cal(choice)