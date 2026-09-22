# 반복문을 사용해서 1-100까지 합을 출력하시오.

# 200을 넘는 시점의 i의 값과 i번째 합계를 출력하시오.


# 200을 넘는 이전 시점의 i,합계를 출력하시오


# 구구단을 출력하시오.
# name = [] # 리스트 일때만 반복문을 사용할수 있음
# kor = []
# stu = []
# for i in range(2):
#     name.append(input("이름입력 : "))
#     kor.append(input("국어점수 입력 : "))

# for i in range(2):
#     print("{}\t{}".format(name[i],kor[i]))

# # (변수한개에 한개값을 받으면 format(1,2,3,4)개수에 맞게 집어 넣어야함)

# stu = []
# for i in range(2):
#     name = input("이름입력 : ")
# kor = int(input("국어점수 입력 : "))
# str.append([name,kor])

# for i in range(2):
#     print("{}\t{}".format(name[i],kor[i]))


stu = []
for i in range(100):
    no = i+1
    name = input("이름입력 : ")
    kor = int(input("국어점수 입력 : "))
stu.append([no,name,kor])

for i in range(2):
    print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))



