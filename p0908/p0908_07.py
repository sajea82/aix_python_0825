# 다른폴더에 있을 경우 : from import해야 함.
# from 폴더명 import 파일명
from project import students
from project import student


stus = students.Students()
# stus.slist = [] 
print(len(stus.slist))

s1 = students.Students(1,"홍길동",100,100,99)
stus.add(s1)
stus.add(students.Students(2,"유관순",100,100,99))

stus.print()


