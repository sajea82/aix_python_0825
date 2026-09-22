# 예외처리 - try - except


choice = int(input("원하는 번호입력 :"))
if choice == 1:
    print("학생성적입력부분")
elif choice == 2:
    print("출력")
elif choice == 3:
    print("수정")
elif choice == 4:
    raise NotImplementedError # 프로그램 구현안된부분 확인



# print(1)
# print(2)
# print(3)
# raise NotImplementedError # 프로그램을 멈춤.
# print(4)
# print(5)
# print(6)
# print(7)




# print(1)

# try:
#     print(2)
#     print(3)
#     print(10/0) # 에러가남.
#     print(4) 
# except Exception as e: # as e - 구문을 보여줌
#     print(e) # 에러가 나는 이유 표시 
#     print(type(e)) # 에러가 나는 이유 표시 
#     print(5) # try - 에러가 나야 돌아감 
#     print(6)
# print(7)


#pront(1) # 구문오류

# 런타임 에러
# arr = [1,2,3,4,5]
# while True:
#     try:
#         choice = int(input("0-4까지 숫자입력 : "))
#         print("선택값 : ",arr[choice])
#     except Exception as e: # Exception as e:(어디가 에러인지 알려줌)
#         print("에러가 났습니다.")
#         print(e)

# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0-4까지 숫자입력 : "))
#     if choice.isdigit():
#         choice= int(choice)
#     else:
#         print("숫자만 입력이 가능합니다. 다시 입력하세요.")
#         continue
#     print("선택값 : ",arr[choice])



