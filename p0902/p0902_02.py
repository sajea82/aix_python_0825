### 앞뒤공백제거 - strip()
a = "       abc      "
print(a)
print((a.strip())) # 공백제거 -> a반영은 안됨.
print(a)

### 중간공백제거 - replace()
b = "   a     b"
print(b.strip())
print(b.replace(" ",""))

### 분리 : split - 리스트타입으로 전달됨.
c = "딸기,수박,바나나,사과"
print(c)
print(c.split(","))



d = "1,홍길동,100,100,100,300,100.0"
dlist = d.split(",")
dlist[2] = 90
dlist[3] = int(dlist[3])
dlist[4] = int(dlist[4])
dlist[5] = dlist[2]+dlist[3]+dlist[4]
dlist[6] = dlist[5]/3

dlist2 = [str(i) for i in dlist]
print(dlist)

# 특정문자로 결합- join "1"+1
# 문자열리스트만 변경가능 join결합
# 문자열로 변환됨
d_str = ",".join(dlist)
print(d_str)

# 5. count : 문자열안에 해당문자가 몇개 있는지 확인
# 6. find : 문자열안에 해당문자가 위치 반환, 없으면 -1
# 7. index : find와 동일, 없으면 에러


# # join
# aa = "/"
# bb = aa.join(["바나나","딸기","사과"])
# print(bb)
# print(type(bb))


# ss = "  파이썬"       #파이썬 - strip
# ss = "<<<<파<<이<썬"   #파이썬 - replace
# print(ss.strip())
# print(ss.strip("<<",""))

# aa = input("이름을 입력하세요.>>").strip() # strip() 공백제거 많이사용

# aa = [1,2,   3, 4 ,5]

# ss = "파이썬 공부 !! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부")) # 4
# print(ss.find("자바")) # 없을때 : -1
# print(ss.index("자바")) # index는 없을때 에러


# aa = "a/b/c/d/e/f/g"
# aa_list = aa.split("/")
# print(aa_list)

# bb = "100,10,5,4,1"
# # 모든수의 합을 구하시오.
# bb_list = bb.split(",")
# bb_list2 = [int(i) for i in bb_list]
# sum = 0 
# for b in bb_list:
#     sum += b
# print(bb_list)
# print("합계 : ",sum)

# find() index() 찾을때

# bb_list2 = [int(i) for i in bb_list] # 문자열을 숫자로 한꺼번에 변경
# print(bb_list2)


# aa = "가나다라가가가나나다라라라라라라라"
# ##
# # {가:10,나:5,다:11...}

# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] += 1
#         print("있습니다.")

# print(aa_dic)


# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

# c = list(zip(a,b))
# d = dict(zip(a,b))
# print(c)
# print(d)

# [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)] # 튜플 

# for i,j in zip(a,b):
#     c.append([i,j]) # 리스트를 2개을  돌릴때 사용
# print(c)

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)


# for i in a: # 리스트를 1개를 돌림
#     for j in b:
#         pass

# 리스트 생성방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0] # 리스트내포
# print(a4)


# # aa = ["바나나","딸기","사과","딸기","딸기","사과"] 키값
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3] # 주소
# # print(aa.count("사과")) # 개수출력
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] = aa_dic[a]+1  # 리스트안에 중복값을 출력 
#         print("있습니다.")

# print(aa_dic)

# pop() : ()괄호안에 숫자입력을 하지 않으면 맨 마지막이 지워진다.

# # 딕셔너리
# a_dic = {"바나나":1,"딸기":3,"사과":2}

# # 출력
# print(a_dic["바나나"]) 

# # 추가
# a_dic["배"] = 5 # 없는 키에 값을 입력
# print(a_dic)

# # 삭제
# del a_dic["바나나"]
# print(a_dic)

# # 수정
# a_dic["사과"] = 100
# print(a_dic)



# a = 10
# a2 = 0
# a2 = a
# print(a2)
# a = 100
# print(a2)


# alist = [1,2,3]
# alist2 = []
# alist2 = alist      # 얕은복사
# # alist2 = [*alist] # 깊은복사(값이 바뀌지 않는다)
# print(alist2)  # 1,2,3


# alist[0] = 100
# print(alist2)
