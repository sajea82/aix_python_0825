# input() 함수
# intput -> 프롬프트에 format 뜻 : 입력해주세요 (입력을 요청하는 문자열)
# 예 시 : 
# input("입력해주세요: ")
# input(">>> ")

# 결 과 :
# 입력해주세요: 이름
# >>> ok

# print(input("입력해주세요: ")) # 함수의 결과 = 함수의 리턴값
# a = input(">>>")
# print(a)
# print(type(a)) 
# 입력에 10 숫자를 넣어도 숫자가 아닌 문자열 str로 자료형 타입이 나온다
# input() 함수의 결과는 "무조건" 문자열로 나온다

# a = input("숫자1: ")
# b = input("숫자2: ") 

# print(a + b)

# 결과값 :
# 숫자1: 10
# 숫자2: 20
# 1020 # 숫자 + 숫자 의 합이아닌 문자와 문자의 합인 1020 결과가 나온다

# 문자열을 숫자로 변환하기
# 숫자로 변환하기 위해 쓸수 있는 함수는 (int, float)가 있다

# print(int("52")) # 정수
# print(float("52.273")) # 실수

# 결과 :
# 52
# 52.273 # " " 문자열이 사라지고 숫자가 나타남

# print(int("hello")) # 문자를 숫자로 변환이 안되기 때문에
# 결과 : ValueError: invalid literal for int() with base 10: 'hello'
# 정수가 아닌 실수를 넣어도 에러가 뜸

# #### 변환예시
# a = input("숫자1: ")
# b = input("숫자2: ")

# ## 문자열 -> 숫자
# a = int(a)
# b = float(b)

# ## 숫자 -> 문자열
# c = str(a)

# print(a + b)
# print(c, type(c))

# 결과 : 
# 숫자1: 52
# 숫자2: 10
# 62.0
# 52 <class 'str'>

# 요점정리
# input()함수 : 입력을 받음
# int()함수 : 정수로 변환
# float()함수 : 부동소수점으로 변환
# str()함수 : 문자열로 변환

# 누적예제
# 프로그램 정의 : 입력, 처리, 출력

# 입력 : inch 단위의 입력
# a = input("inch 단위 숫자:")

# 처리 : inch -> cm 변환하는 처리
# a = float(a) * 2.54

# 출력 : cm 단위를 출력
# print("cm 단위로는", a, "입니다")
# print(a) 결과 : 76.2

# 결과 : 
# inch 단위 숫자:30
# cm 단위로는 76.2 입니다

# 문제 : inch 단위의 자료를 입력받아 cm 단위를 구해라
# str_input = input("숫자 입력>")
# num_input = float(str_input) # 숫자로 변환을 하기 위해서는\
                               # (int, float)둘중 한가지를 사용하면 된

# print()
# print(num_input, "inch")
# print((num_input * 2.54),"cm")
# 결과 : 
# 숫자 입력>30

# 30.0 inch
# 76.2 cm

# a = input("숫자입력")
# b = float(a)

# print()
# print(b, "inch")
# print((b * 2.54), "cm")

# # (문제) : 원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드입니다. 
# # 둘레 : 2 * 원주율 * 반지름
# # 넓이 : 원주율 * 반지름 * 반지름
# 입력 
# a = input("원의 반지름>")
# a = float(a)
# 처리, 출력
# pi = 3.14 # 원주율
# print("둘레: ",2 * pi * a ) 
# print("넓이: ",pi * (a ** 2))

# 동영상 문제풀이
# 입력 : 반지름 입력
# r = input("반지름: ")
# r = float(r)

# 처리 : 둘레와 넓이를 구한다.
# pi = 3.14
# 둘레 = 2 * pi * r
# 넓이 = pi * (r ** 2)

# 출력 : 둘레와 넓이를 출력한다.
# print("둘레:", 둘레)
# print("넓이:", 넓이)
