my_info = {"id":"aaa","pw":"1111",\
        "money":10_000_000}

cart = []

s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

print("1.컴퓨터-1000000")
print("2.냉장고")
print("3.오디오")
print("4.세탁기")

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
print("-"*40)
choice = int(input("원하는 번호입력 : "))
print()
while True:
    print()
    print("[ 쇼핑몰 구매사이트 ]")
    for i,j in enumerate(s-arr):
        print(f"{i+1}. {p['p_name']} : {p['price']:,}원")
    print("-"*30) 
    print()

    if choice == 1:
        no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0) "))
        if no == 1:
            print("구매완료")
            my_info["money"] -= s-arr[0]['price']
    elif choice == 2:
        print("냉장고")
    elif choice == 3:
        print("오디오")
    elif choice == 4:
        print("세탁기")
