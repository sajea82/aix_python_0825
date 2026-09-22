# 두수를 입력받아 합을 구하는 무한반복 프로그램을 구현하시오
while True:
    a = int(input("1.숫자 : "))
    if a==0: break   
    b = int(input("2.숫자 : "))
    if b==0: break
    print("{}+{}={}".format(a,b,a+b)) # 합

print("프로그램 종료")



# # break : 반복문(for,while)을 종료시켜줌.

# i = 0
# while True:
#     print(i)
#     if i%10==0:
#         input1 = input("프로그램을 종료할까요?")
#         if input1 == "x":
#             break
#     i += 1

# print("프로그램종료")


# # for i in range(10):
# #     print(i)

# # i = 0 # 초기값
# # while i<10: # 조건식
# #     print(i)
# #     i += 1 # 증감식

# alist = ["바나나","딸기","수박"]

# i = 0
# while i<3:
#     print("{}:{}".format(i,alist[i]))
#     i += 1

# for i in alist:
#     print("{}:{}".format(i,alist[i]))


# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# print("-"*50)
# i = 1
# while(i<11): # 조건식이  True 일때만 실행
#     print(i)
#     i += 2

# # 모든 for문은 while 변경 가능함
# # for : 반복,구간지정 1-10 까지
# # while : 조건식이 있을때, 주로 사용, 무한반복일때 사용

# i = 0
# while True:
#     print(i)
#     i += 1

# # while 문을 사용해서 alist 있는 값을 출력하시오
# # 1 2 3 4 5 ....9
# alist = list(range(10))

# i = 0
# while i<10:
#     print(alist[i],end=" ")
#     i += 1
#     # i값을 증가




