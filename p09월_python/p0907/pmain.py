from pfunc import*

readStu() # 등수

while True:
    choice = main_screen() # 메인입력

    if choice == 1:
        stu_input() # 학생성적 입력

    elif choice == 2:
        stu_output() # 학생성적 출력

    elif choice == 3:
        pass

    elif choice == 9:
        writeStu() # 학생성적파일 저장하기

    else:
        print(" 프로그램을 종료 ")
    