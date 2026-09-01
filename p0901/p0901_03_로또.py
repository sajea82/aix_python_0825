# 로또맞추기
# 1. 랜덤번호 6개 생성
# 2. 입력번호 6개 생성
# 3. 랜덤본호, 입력번호 생성
# - for 입력번호 1개 가져와서 랜덤번호 리스트와 비교
# - 있는 번호를 리스트에 추가
# 4. 결과 출력


import random
lotto = random.sample(range(1,46),6)
print("확인 : ",lotto)

in_arr = []
no = []
for i in range(6):
        no = int(input("1-45사이 숫자입력 : "))
        in_arr.append(no)
    ## no = input("1-45사이 숫자입력 : ") # 문자열
    ## 10a
    ## if no.isdigit(): #문자열을 숫자로 변경가능한지()
    ##     no = int(input("1-45사이 숫자입력 : "))
    ##     in_arr.append(no)

answer_arr = [] # 비교
for i in in_arr:
    if i in lotto:
        answer_arr.append(i)

# 결과출력
print("로또번호 : ",lotto)
print("입력번호 : ",in_arr)
print("정답객수 : ",len(answer_arr))
print("정답번호 : ",answer_arr)