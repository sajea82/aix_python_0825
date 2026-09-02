# import random
# import datetime #현재시간을 가져오는 클래스선언
# # from datetime import datetime

# # 현재시간
# now = datetime.datetime.now()
# print("전체:",now)       #전체시간
# print("년도:",now.year)  #년도
# print("월:",now.month) #월
# print("일:",now.day)   #일
# print("시:",now.hour)  #시
# print("분:",now.minute) #분
# print("초:",now.second) #초

import datetime
now = datetime.datetime.now()
print(now)      
print(now.year) 
print(now.month) 
print("{:02d}월".format(now.month))
print("{:02d}월".format(now.second))

# 2026년8월27일 11시57분20초
print(now)
f_date = now.strftime("%y년%m월%d일 %m시%s초") 
print(f_date)

print("{}년{}월{}일 {}시{}분{}초".format(\
    now.year,now.month,now.day,now.hour,\
        now.minute,now.second))



# 월 출력하는데 , 1,2,3.....9월 1월,2월

# 전체시간
# print("년도:",now.year)  #년도
# print("월:",now.month) #월
# print("일:",now.day)   #일
# print("시:",now.hour)  #시
# print("분:",now.minute) #분
# print("초:",now.second)))

# # 2026년8월27일 11시12분10초
# print("{}년{}월{}일 {}시{}분{}초".format(\
#     now.year,now.month,now.day,now.hour,\
#     now.minute,now.second))

# # format
# # 123 -> 5자리 빈공백 0으로 채워서 출력하시오.
# print("{:015,d}".format(123456789))
# print("{:02d}".format(12))
