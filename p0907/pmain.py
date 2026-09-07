from p_stu_m import*

readStu() # 등수

while True:
    choice = main_screen() # 메인입력

    if choice == 1:
        stu_input() # 학생성적 입력

    if choice == 2:
        stu_output() # 학생성적 출력

    if choice == 3:
        pass

    if choice == 9:
        writeStu() # 학생성적파일 저장하기









                