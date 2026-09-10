stu = []
sno = 1

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적저장")
    print("0. 프로그램종료")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()

    if choice == 1:
        while True:
            no = sno
            print("[ 학생성적입력 ]")
            name = input(f"{no}")
