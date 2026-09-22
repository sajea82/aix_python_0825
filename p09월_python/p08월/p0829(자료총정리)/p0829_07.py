# find()와 rfind() : 문자열에서 문자 탐색
# a = "abcabcabcd"
# # 왼쪽부터 탐색
# find = a.find("b")
# # 오른쪽부터 탐색
# rfind = a.rfind("b")
# print(f"{find},{rfind}")
# 결과 : 1,7

## 문자열의 in 연산자 : 앞에 있는게 뒤에 있는지를 물어보는것
# print("안녕" in "안녕하세요") # True
# print("잘가" in "안녕하세요") # False

# # 정수
# "{:d}".format(52)
# # 실수
# "{:f}".format(52)

# {:.1f} : 소수점이하 1개까지만 출력
# {:.2f} : 소수점이하 2개까지만 출력



# # 특정 칸만큼 출력
# print("{:5d}".format(52))
# print("{:5d}".format(-52))
# print("{:=+5d}".format(52))
# print("{:=5d}".format(52)) # 부호가 앞으로 붙어서 출력

# # 3장
# # 조건문
# # bool 
# True # 참
# False # 거짓

# # 비교 연산자 : == (같다)
# = # 할당 연산자
# == # 비교 연산자

# # 예시:
# # # x = 20
# # 10 < x < 30
# # 결과 : True

# 논리 연산자
## 단항 not
not True # False
not False # True

# ## 이항 dnd
# True dnd True # True
# True dnd False # False
# False and True # False
# False and False # False

# ## 이항 or
# # 둘 중에 하나만 True 이면 결과 True
# True or True # True
# True or False # True
# False or True # True
# False or False # False

# 기본적으로 둘 다 만족해아 한다 -> and 
#          둘 중 하나만 만족해도 된다 -> or
            
# # 날짜/시간 구하는 방법
# import datetime
# import pytz

# seoul = pytz.timezone("Asia/Seoul")
# now = datetime.datetime.now(seoul)

# print("{}년{}월{}일{}시{}분{}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second,
#     ))

# # if 조건문의 기본조건
# # if 조건 : 
#       문장
#       문장
#       문장

# ## 조건이 True일 때만 들여쓰기 안쪽의 문장을 실행
# if True:
#     print("True입니다.") # True 일때만 실행

# if False:
#     print("False입니다.") # 실행하지 않음  
        
# 양수 음수 0인지 판별하는 프로그램

# # 예시 :
# raw_input = input("정수를 입력해주세요: ")
# raw_input = int(raw_input)

# if raw_input > 0:
#     print("양수입니다.")

# if raw_input < 0:
#     print("음수입니다.")

# if raw_input == 0:
#     print("0입니다.")    

# # 조건문 Suite(복합문장)
# if condition: suite
# if 조건 : 복합문장

# # 복합 문장 : 문장을 묶어 놓는 것
# 문장
# 문장
#     문장 
#     문장 # 들여쓰기로 묶어진 문장으로 인식
# 문장

# IndentationError : 들여쓰기가 알수없는 곳에 있을때