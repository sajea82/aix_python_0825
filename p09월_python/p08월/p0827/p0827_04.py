import datetime
now = datetime.datetime.now()
month = now.month
if month>= 7:
    print("{}월 : 하반기입니다.".format(month))
else:
    print("{}월 : 상반기입니다.".format(month))
    