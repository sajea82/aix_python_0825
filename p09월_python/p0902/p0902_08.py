from func import *  # 다른곳 파일과 연결

# 함수 사용 이유
# 1. 중복되는 코드 재사용
# 2. 코드를 간결하게 하기 위해
# 프로그램 시작------------------>
while True:
    choice = main_print()
    result = ran_number(choice)
    print("결과 : ",result)

