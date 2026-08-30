# for i in range(1,10):
#     print(f"2 X {i} = {2*i}")

# for i in range(2,10):          # 구구단 출력 꼭 외울것 format(i,j,i*j)
#      for j in range(1,10):
#          print("2 X {} = {}".format(i,i*2)) 


# for i in range(1,4):        # 3번돌고
#     for j in range(1,10):   # 9번돌다
#         print(i,j)          # i 3번돌때 j는 9번돈다 총 27번 돈다

# for i in range(0,10):     
#     for j in range(0,10):
#         for k in range(0,10):  
#             print(i,j)          

# # 번호표 출력
# for i in range(0,10):     
#     for j in range(0,10):
#         for k in range(0,10):
#             print("{}{}".format(i,j,k)) 



# for i in range(1,10):
#     print(f"2 X {i} = {2*i}") # 구구단이 출력


# sum = 0
# for i in range(1,11): # 1부터 10까지 출력 
#     sum = sum+i  
# print("합계 : ",sum) # 55출력 적은수로 2번은 검증후 사용 ** 중요 꼭 외울것

# sum 100넘어가는 시점은 i가 얼마일때 일까요?
# 
sum = 0
for i in range(1,11):
    sum = sum+i
    if sum>11:
        print("10보다 크기 바로앞일때 :",i-1)
        print("10초과전 시점 : ",sum)
        break



# print("1",end="\t") #end 옆으로 출력 \t 탭
# print("2")
# print("3")



# for i in range(3): # 입력하고 출력
#    no = i+1
# #    print(i+1,"번째")
#    name = input("이름 입력 : ")
#    kor = int(input("국어점수 입력 : "))
# # print("번호 :",i+1,end="\t") # 옆으로 출력
#    print("{}\t{}\t{}".format(no,name,kor))









# for i in range(10):
#     print("안녕")

# for _ in range(10):
#     print("안녕")




# # for 변수 in 범위 :
# for i in range(5): # for 
#     print(i)

# for i in range(5):
#     print(i*10)

# for i in range(0,10,2): # 1시작 11까지 2칸씩 리스트와 같음 [] 여기서는 ,
#     print(i)

# for i in [1,5,3,2]:
#     print(1)

# for i in "안녕하세요.":
#     print(i)


# arr = list(range(1,11)) # range 범위
# print(arr)



