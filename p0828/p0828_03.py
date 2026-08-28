str1 = "안녕" # 문자열
nit = 1  # 숫자-정수형
float1 = 1.1 # 숫자 - 실수형
bool = True # 불형

# 리스트 - 모든타입이 들어올수 있음(리스트안에 리스트가능)
arr = [str1,nit1,float,bool1,[1,2,3,"안녕"]]

# 자료형 확인 - type()
print(int(float1))

## 타입변환
str2 = "111"
print(type(str2))
print(type(int(str2))) # 문자열을 정수타입을 변경
# int()- 정수타입변환, float()-실수,stra()-문자열,bool()-불타입

# 문자열 선언 - "",''

# ""출력하고 싶을때
print("안녕 나는 \"홍길동\"이라고 해.")
print('안녕 나는 "홍길동"이라고 해.')

# \t:탭, \n:줄바꿈
print("안녕\n하세요")

# 문자열 -,+:연결연산자, #:반복
print("안녕"+"하세요")
#print("안녕"+2) # str타입 + int타입 에러
print("안녕"*10) # 반복

# 문자슬라이싱
str1 = "안녕하세요"
print(str1[1])

# [시작:끝:간격]
print(str1[::-1]) # 반대로 출력
print(str1[:-1]) # 제일뒤에 빼고 출력
print(str1[::2]) # 2칸씩 띄워서 출력


# print(str1[10]) # 에러

print(len(str))





