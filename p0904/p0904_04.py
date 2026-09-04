# 파일을 읽어오기
f = open("C:\\aaa\\test1.txt","r",encoding="utf-8") # \\(문자로 읽어오기)->/대체
while True:
    line = f.readline()
    if not line: break
    print(line,end="")
f.close()


# f1 = file1.readline() # 1줄출력
# print(f1,end="")
# f2 = file1.readline()
# print(f2,end="")
# f3 = file1.readline()
# print(f3,end="")