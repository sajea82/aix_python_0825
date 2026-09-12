# 1. 먼저 전체 프로그램 구조부터 이해하기
# 현재 프로그램은 크게 4개의 파일로 나뉘어 있습니다.

# python
# │
# ├─ main.py
# │    ↓
# │  프로그램 시작
# │
# ├─ stuFunc.py
# │    ↓
# │  학생성적 관련 함수
# │
# ├─ student.py
# │    ↓
# │  Student 클래스
# │  학생 한 명
# │
# ├─ students.py
# │    ↓
# │  Students 클래스
# │  여러 학생 관리
# │
# └─ stu.txt
#      ↓
#    학생 데이터 저장

# 전체 흐름은:

# main.py
#    ↓
# main_screen()
#    ↓
# 사용자 선택
#    ↓
# ┌───────────────┐
# │ 1. 입력       │ → stu_input()
# │ 2. 출력       │ → stu_output()
# │ 3. 수정       │ → stu_update()
# │ 8. 등수       │ → rank()
# │ 9. 저장       │ → writeStu()
# └───────────────┘
#    ↓
# Students 객체
#    ↓
# slist
#    ↓
# Student 객체들

# 이 구조를 먼저 머릿속에 넣으세요.

# 2. 초보자가 공부할 파일 순서
# 현재 파일들을 코드가 쉬운 순서로 공부하면:

# ① main.py
# 가장 먼저 봅니다.

# 공부할 내용:

# from stuFunc import *
# while True:
# if
# elif
# else
# break

# 여기서는 프로그램 전체 흐름을 이해하는 것이 목적입니다.

# 아직 class의 내부 동작까지 이해할 필요는 없습니다.

# ② stuFunc.py
# 두 번째로 공부합니다.

# 이 파일이 가장 중요합니다. ⭐⭐⭐⭐⭐

# 여기에는 지금까지 배운 거의 모든 문법이 들어 있습니다.

# readStu()
# writeStu()
# main_screen()
# stu_input()
# stu_output()
# stu_update()

# 여기서 공부해야 하는 것:

# 변수
# input()
# print()
# if
# for
# while
# break
# global
# 리스트
# 딕셔너리
# 함수
# return
# 파일 입출력
# 문자열
# split()
# strip()
# open()
# ③ student.py
# 세 번째입니다.

# 여기서부터 클래스 공부를 시작합니다.

# class Student:

# 중점적으로:

# class
# __init__()
# self
# 객체
# 속성
# 메서드

# 를 공부합니다.

# ④ students.py
# 네 번째입니다.

# class Students:

# 여기서는 객체를 여러 개 관리하는 방법을 공부합니다.

# self.slist = []

# 그리고:

# self.slist.append(s)

# 를 이해하는 것이 중요합니다.

# 3. main.py에서 공부할 문법
# 현재 메인 프로그램:

# from stuFunc import *

# readStu()

# while True:
#     choice = main_screen()

#     if choice == 1:
#         stu_input()
#     elif choice == 2:
#         stu_output()
#     elif choice == 3:
#         stu_update()
#     elif choice == 8:
#         print("[등수처리]")
#     elif choice == 9:
#         writeStu()
#     else:
#         print("프로그램 종료")
#         break

# 여기서 우선 알아야 할 것은:

# import
# from stuFunc import *

# 다른 파일의 기능을 가져오는 것입니다.

# 처음에는 import의 모든 종류를 공부할 필요 없습니다.

# 일단:

# import
# from ~ import

# 정도만 알아두세요.

# while
# while True:

# 조건이 참인 동안 반복합니다.

# if / elif / else
# 메뉴 선택에 사용합니다.

# break
# 반복문을 종료합니다.

# 4. stuFunc.py에서 공부해야 할 문법
# 여기가 가장 중요한 공부 장소입니다.

# ① 변수
# stuNum = 1

# 변수가 무엇인지 알아야 합니다.

# ② 입력
# name = input("학생이름 : ")

# 그리고:

# kor = int(input("국어 : "))

# 여기서 아주 중요한 개념:

# input()
#    ↓
# 문자열
#    ↓
# int()
#    ↓
# 정수

# ③ 리스트
# 클래스 적용 전에는:

# stuList = []

# 였습니다.

# 학생 추가:

# stuList.append(stu)

# 학생 반복:

# for s in stuList:
#     print(s)

# 이것은 반드시 이해하세요.

# 반드시 알아야 하는 리스트 메서드
# append()
# insert()
# remove()
# pop()
# sort()
# reverse()
# clear()

# 그리고 함수:

# len()

# 5. 딕셔너리는 반드시 공부하세요
# 클래스 적용 전 코드에서:

# stu = {
#     "no": no,
#     "name": name,
#     "kor": kor,
#     "eng": eng,
#     "math": math,
#     "total": total,
#     "avg": avg,
#     "rank": rank
# }

# 이 구조가 중요합니다.

# 접근:

# stu["name"]
# stu["kor"]

# 수정:

# stu["kor"] = 90

# 반드시 익힐 것:

# keys()
# values()
# items()
# get()

# 특히:

# for key, value in stu.items():
#     print(key, value)

# 를 이해하면 좋습니다.

# 6. 함수 공부
# stuFunc.py의 핵심입니다.

# 예:

# def stu_input():
#     ...

# 호출:

# stu_input()

# 여기서 반드시 알아야 하는 것:

# def
# 매개변수
# 인자
# return
# 지역변수
# 전역변수
# global

# 특히 return을 중요하게 공부하세요.

# 예:

# def add(a, b):
#     result = a + b
#     return result

# 사용:

# x = add(10, 20)
# print(x)

# 7. global은 이해하되 너무 의존하지 마세요
# 현재 코드에는:

# global stuNum

# 이 있습니다.

# 초보자는 이것을 이해해야 하지만 많이 사용하는 것을 목표로 하면 안 됩니다.

# 현재:

# stuNum = 1

# def stu_input():
#     global stuNum

# 형태인데, 함수가 많아질수록 전역변수 관리가 어려워집니다.

# 나중에는 클래스나 함수의 매개변수를 이용하는 방식으로 개선합니다.

# 8. 파일 입출력은 꼭 공부
# 현재:

# with open("c:/aaa/stu.txt", "r", encoding="utf-8") as f:

# 가 있습니다.

# 이것은 매우 중요한 문법입니다.

# 먼저:

# open()

# 을 공부합니다.

# 그리고:

# r → 읽기
# w → 쓰기
# a → 추가

# 를 기억하세요.

# 읽기
# with open("test.txt", "r", encoding="utf-8") as f:
#     data = f.read()

# 한 줄 읽기
# f.readline()

# 쓰기
# f.write("홍길동\n")

# 현재 프로그램의:

# str = f.readline()

# 과:

# f.write(str + "\n")

# 를 이해할 수 있어야 합니다.

# 9. 문자열 함수
# 현재 파일에서:

# stu = str.split(",")

# 가 있습니다.

# 예:

# data = "1,홍길동,90,80,70"

# data.split(",")

# 결과:

# ["1", "홍길동", "90", "80", "70"]

# 반드시 공부
# split()
# strip()
# replace()
# lower()
# upper()

# 이 정도면 충분합니다.

# 10. student.py — 클래스 공부 시작
# 이제 클래스로 넘어갑니다.

# 현재:

# class Student:

#     def __init__(self, no, name, kor, eng, math):
#         self.no = no
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math

# 이걸 처음 보면 어렵습니다.

# 다음처럼 이해하세요.

# Student = 학생을 만드는 설계도

# 그리고:

# s = Student(1, "홍길동", 90, 80, 70)

# 하면 실제 학생 객체가 하나 만들어집니다.

# s
#  ↓
# Student 객체
#  ├─ no = 1
#  ├─ name = 홍길동
#  ├─ kor = 90
#  ├─ eng = 80
#  └─ math = 70

# 11. self는 특히 중요
# 처음에는 가장 헷갈리는 부분입니다.

# self.name = name

# 이것을:

# 오른쪽 name
# → 함수로 전달받은 값

# 왼쪽 self.name
# → 만들어진 학생 객체의 이름

# 이라고 이해하면 됩니다.

# 예:

# s = Student(1, "홍길동", 90, 80, 70)

# 그러면:

# s.name

# 은:

# 홍길동

# 입니다.

# 12. __init__()도 반드시 공부
# def __init__(self, ...):

# 객체를 만들 때 자동으로 실행되는 함수입니다.

# s = Student(...)

# 하면 __init__()이 실행됩니다.

# 현재 코드에서는 학생의 정보를 초기화하는 역할입니다.

# 13. s_total(), s_avg()는 메서드
# 현재:

# def s_total(self):
#     self.total = self.kor + self.eng + self.math

# 이것은 학생 객체가 가지고 있는 기능입니다.

# 호출:

# s.s_total()

# 그리고:

# s.s_avg()

# 즉:

# 함수
#  ↓
# 객체 안에 들어가면
#  ↓
# 메서드

# 라고 생각하면 됩니다.

# 14. students.py는 그 다음
# 현재:

# class Students:
#     slist = []

#     def add(self, s):
#         self.slist.append(s)

# 여기서는:

# Student → 학생 한 명
# Students → 학생 여러 명

# 이라는 개념이 중요합니다.

# 예:

# s1 = Student(1, "홍길동", 90, 80, 70)
# s2 = Student(2, "김철수", 80, 90, 80)

# stus = Students()

# stus.add(s1)
# stus.add(s2)

# 그러면:

# stus
#  ↓
# Students
#  ↓
# slist
#  ↓
# ┌─────────────┐
# │ Student     │
# │ 홍길동      │
# ├─────────────┤
# │ Student     │
# │ 김철수      │
# └─────────────┘

# 입니다.

# 15. 지금 당장 공부하지 않아도 되는 것
# 초보자라면 아래 내용은 잠시 미뤄도 됩니다.

# 아직 미뤄도 됨
# lambda
# map()
# filter()
# reduce()
# decorator
# generator
# iterator
# 재귀함수
# 상속
# 다중상속
# 추상클래스
# @property
# __new__()
# __repr__()
# 패키지 구조
# typing
# dataclass

# 특히:

# lambda

# 가 나온다고 무조건 외우려고 하지 마세요.

# 현재 등수 처리에서:

# sorted(stuList, key=lambda s: s.total)

# 같은 코드가 나오더라도 sorted()를 먼저 이해하고 lambda는 나중에 이해해도 됩니다.

# 16. 반드시 외워야 하는 함수
# 초보 단계에서는 아래 정도를 목표로 하세요.

# ⭐⭐⭐⭐⭐ 최우선
# print()
# input()
# len()
# range()
# int()
# float()
# str()
# type()

# 리스트
# append()
# insert()
# remove()
# pop()
# sort()
# reverse()
# clear()

# 딕셔너리
# keys()
# values()
# items()
# get()

# 문자열
# split()
# strip()
# replace()
# lower()
# upper()

# 파일
# open()
# read()
# readline()
# readlines()
# write()

# 나중에
# sorted()
# enumerate()

# 그리고:

# lambda

# 는 외우는 것보다 사용 이유를 이해하는 것이 중요합니다.

# 17. 1주차 — 파이썬 기본기
# 목표
# 혼자서 간단한 프로그램을 만들 수 있는 수준.

# 공부:

# 변수
# 자료형
# input()
# print()
# 연산자
# if
# elif
# else
# for
# while
# break

# 연습문제 1
# 학생 이름과 국어/영어/수학 점수를 입력받아:

# 이름 : 홍길동
# 국어 : 90
# 영어 : 80
# 수학 : 70

# 이름 : 홍길동
# 합계 : 240
# 평균 : 80.00

# 출력하세요.

# 연습문제 2
# 점수에 따라:

# 90 이상 → A
# 80 이상 → B
# 70 이상 → C
# 60 이상 → D
# 그 외 → F

# 를 출력하세요.

# 연습문제 3
# 1부터 10까지 출력하세요.

# 그리고:

# 1 + 2 + ... + 10

# 의 합을 구하세요.

# 18. 2주차 — 리스트와 딕셔너리
# 목표
# 여러 학생을 저장하고 처리하기.

# 먼저:

# stuList = []

# 그리고:

# stuList.append(...)

# 를 익힙니다.

# 연습문제
# 학생 3명을 딕셔너리로 저장하세요.

# stu1 = {
#     "name": "홍길동",
#     "kor": 90,
#     "eng": 80,
#     "math": 70
# }

# 3명을 stuList에 저장하고:

# 홍길동 90 80 70
# 김철수 80 90 90
# 이영희 70 80 80

# 형태로 출력하세요.

# 그 다음 모든 학생의 합계와 평균을 계산하세요.

# 19. 3주차 — 함수
# 목표
# 반복되는 코드를 함수로 분리하기.

# 먼저:

# def stu_input():

# 그리고:

# def stu_output():

# 을 만들어봅니다.

# 최종적으로:

# main
#  ├─ stu_input()
#  ├─ stu_output()
#  ├─ stu_update()
#  └─ stu_rank()

# 구조를 만드는 것이 목표입니다.

# 연습문제
# 다음 함수를 직접 만들어보세요.

# def add(a, b):

# def average(total, count):

# def check_score(score):

# 그리고 return을 사용하세요.

# 20. 4주차 — 파일 입출력
# 목표
# 프로그램을 종료해도 학생 데이터가 사라지지 않게 만들기.

# 먼저:

# with open("stu.txt", "w", encoding="utf-8") as f:

# 를 연습합니다.

# 학생 데이터를:

# 1,홍길동,90,80,70
# 2,김철수,80,90,80

# 형태로 저장하세요.

# 그 다음 파일을 읽어서:

# f.readline()

# 으로 한 줄씩 가져옵니다.

# 그리고:

# split(",")

# 으로 분리합니다.

# 이 단계가 현재 readStu()를 이해하는 핵심입니다.

# 21. 5주차 — 클래스
# 이제 student.py를 공부합니다.

# 목표:

# class Student:

# 를 이해하는 것.

# 직접 다음 클래스를 만들어보세요.

# class Student:

#     def __init__(self, name, kor, eng, math):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math

#     def total(self):
#         return self.kor + self.eng + self.math

#     def avg(self):
#         return self.total() / 3

# 그리고:

# s = Student("홍길동", 90, 80, 70)

# 으로 객체를 만들어보세요.

# 22. 6주차 — 현재 프로젝트 완성
# 이제 현재 코드를 다시 봅니다.

# Student
#    ↓
# 학생 한 명

# Students
#    ↓
# 학생 여러 명

# stuFunc
#    ↓
# 학생 관리 기능

# main
#    ↓
# 프로그램 실행

# 그리고 다음 기능을 완성합니다.

# 1. 성적입력
# 2. 성적출력
# 3. 성적수정
# 8. 등수처리
# 9. 파일저장
# 0. 종료

# 이 단계까지 오면 지금 올려주신 코드가 훨씬 쉽게 보일 겁니다.

# 23. 가장 중요한 공부 방법
# 지금 학생 성적 프로그램을 공부하면서 코드를 그대로 베껴서 실행하는 것은 효과가 낮습니다.

# 다음 순서로 하세요.

# ① 코드를 보고 설명하기
# 예를 들어:

# for s in stus.slist:
#     print(s)

# 를 보고

# "stus 안에 있는 학생 리스트에서 학생을 하나씩 꺼내서 s에 넣고 출력한다."

# 라고 말할 수 있어야 합니다.

# ② 코드를 안 보고 직접 작성하기
# for s in stus.slist:
#     print(s)

# 를 가리고 직접 작성해보세요.

# ③ 일부러 수정하기
# 예를 들어:

# kor = int(input("국어 : "))

# 를:

# kor = int(input("국어 점수 : "))

# 로 바꿔보세요.

# ④ 오류를 일부러 만들어보기
# 예:

# kor = input("국어 : ")
# eng = 80

# print(kor + eng)

# 왜 오류가 발생하는지 생각해보세요.

# 이런 과정이 암기보다 훨씬 중요합니다.

# 24. 최종 학습 로드맵
# 전체를 한 장으로 정리하면:

# [1단계]
# 변수 / 자료형
#    ↓
# input / print
#    ↓
# 연산자
#    ↓
# if
#    ↓
# for / while
#    ↓

# [2단계]
# list
#    ↓
# dict
#    ↓
# 문자열
#    ↓
# split / strip
#    ↓

# [3단계]
# 함수
#    ↓
# 매개변수
#    ↓
# return
#    ↓
# 지역변수 / 전역변수
#    ↓

# [4단계]
# 파일
#    ↓
# open
#    ↓
# read / readline
#    ↓
# write
#    ↓

# [5단계]
# sorted
#    ↓
# enumerate
#    ↓
# lambda
#    ↓

# [6단계]
# class
#    ↓
# object
#    ↓
# __init__
#    ↓
# self
#    ↓
# 메서드
#    ↓

# [7단계]
# Student
#    ↓
# Students
#    ↓
# 모듈
#    ↓
# import
#    ↓

# [8단계]
# 학생성적프로그램 완성

# ⭐ 가장 중요한 조언
# 현재 코드에서 class Student부터 이해하려고 하지 마세요.

# 지금은 오히려 클래스로 바꾸기 전 코드를 먼저 공부하는 게 좋습니다.

# 즉,

# 딕셔너리로 학생 1명 만들기
#         ↓
# 리스트로 학생 여러 명 관리
#         ↓
# for로 학생 처리
#         ↓
# 함수로 기능 분리
#         ↓
# 파일에 저장/읽기
#         ↓
# Student 클래스로 변경
#         ↓
# Students 클래스로 여러 객체 관리

# 이 순서로 가면 됩니다.

# 그리고 현재 코드에서 가장 먼저 집중할 3가지만 고른다면 list, dict, function입니다. 
# 이 세 가지가 확실해지면 지금 작성하신 stuFunc.py의 상당 부분을 스스로 읽을 수 있게 됩니다.