
# c,자바 : 컴파일러 언어 - 모든소스를 기계어로 번역후 프로그램진행
# 파이썬 : 스크립트 언어 - 한줄씩 기계어로 번역후 프뢰그램진행
# 함수사용이유 : 코드재사용, 코드간결
# 함수는 위에서 함수선언후 함수호출을 해야 읽을수 있다 순서가 바뀌면 실행이 안된다.
def d_print():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")

def cal (n1,n2):
    r1 = n1+n2
    r2 = n1-n2
    r3 = n1*n2
    r4 = n1/n2
    return r1,r2,r3,r4 # return(보내는것)

# ------
hello_print()
d_print()

n1 = int(input("숫자입력 : "))
n2 = int(input("숫자입력 : "))
r1,r2,r3,r4 = cal (n1,n2) # (n1,n2) : 받는것
print(r1,r2,r3,r4)

# print("{}+{}={}".format(n1,n2,n1+n2))
# print("{}-{}={}".format(n1,n2,n1+n2))
# print("{}*{}={}".format(n1,n2,n1+n2))
# print("{}/{}={}".format(n1,n2,n1+n2))


# shift + alt + 방향키 , alt + 방향키

# def d_print():   #: 함수선언
#     for i in range(1,11):
#         print(i)
# # --- 이후 실행
# d_print()    #: 함수호출
