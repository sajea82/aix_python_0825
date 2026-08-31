# 반복문
# for i in range(10)범위/range(1,11)간격/range(1,11,2)/[1,2,3]/"안녕하세요"
# 구구단출력
# for i in range(2,10):
#     print(i,"X",1,"=",i*1)
#     print("{}X{}={}".format(i,1,i*1))
#     print(f"{i}X{1}={i*1}")

# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}X{}={}".format(i,j,i*j),end="  ")
#     print()

for i in range(2,10):
    for j in range(1,10):
        print("{}X{}={}".format(i,j,i*j),end="\t")
    print()




# print(1,end="\t") # 옆으로 출력방법 (end="")
# print(2,end=" ")
# print(3)


# nums = [3,9,10,105,220,2,1]
# for n in nums:
#     print(n)

# 3:홀수
# 9:홀수
# # 10:짝수
# nums = [3,9,10,105,220,2,1]
# for n in nums:
#     # print(n) 
#     #  a = int(input("숫자입력:"))
#     if n%2==0:
#         print(n,": 짝수입니다.")
#     else: pass # 짝수만 출력하고 싶을때         # break (한번돌고 멈춤)
#     #     print(n,": 홀수입니다.")


# # 입력한 숫자가 홀수인지,짝수인지 출력하시오.
# a = int(input("숫자입력:"))
# # %2==0
# if a%2==0:
#      print("짝수입니다.")
# else:
#      print("홀수입니다.")






# for i in "안녕하세요":
#     print(i)




# for i in range(1,11): # 1번 돌고를 11번 (10보다 크면 정지)
#     print(i)


# # 1,2,3,------10 -> 10,20,30,-----100
# for i in range(1,11):
#     print(i*10)

# arr = [1,3,5,7]
# for arr in arr:
#     print(arr)

# fruits = ["사과","배","바나나"]
# for f in fruits:
#     print(arr)



# 이름입력을 3번 반복

# for i in range(3):
#     input("이름입력: ")

# [학생명단]
# 홍길도
# 유관순
# 이순신

# name = []
# for i in range(3):
#     a = input("이름입력:")
#     name.append(a) # 리스트 : append(추가할값), insert, extend

# print("[학생명단]")
# print(name)
# for n in name :
#     print(n)

# # for in (반복문) 범위지정 입력 반목문 3번이상은 안함
# # range(범위)
# for i in range(10): # 0,1,2
#     print(i) 

# for i in range(1,6):
#         print(i)
# print(""*10)
# for i in range(0,11,2):
#       print(i)





