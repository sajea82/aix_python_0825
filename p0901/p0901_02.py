# 1-100사이의 숫자맞추기
# 1. 랜덤번호 1개 생성
# 2. 무한으로 입력받기
# 3. 숫자를 입력 받기 
# 4. 랜덤번와 숫자 비교
# 5. 결과출력

# 입력
import random
ran_no = random.randint(1,100)

# 처리
in_no = 0
in_arr = []
while True:
    in_no = int(input("1-100사이 숫자입력 : "))
    if in_no == ran_no:
        print("정답입니다.")
        break
    elif in_no > ran_no: 
        print(in_no,"")



