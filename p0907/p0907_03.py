m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","' \
'          2.08","4,504,432","4,826,226","          0.93"'
with open("common/stu.txt","a",encoding="utf-8") as f:
    allStr = ""
    no = 0
    while True: # ,1,홍길동,100 / 1,홍길동,100,
        outStr = input("내용입력 : ")
        if no == 0:
            allStr = outStr # 앞에 쉼표를 없앰.
            no += 1 
            continue

        if outStr == "":
            f.write(allStr+"\n")
            break
        allStr += ","+outStr
        no += 1 
    print(allStr)


# common 폴더안에 stu.txt로 파일을 저장하시오.
# 1
# 홍길동
# 100
# 100
# 100
# 300
# 100.0

# with open("common/stu.txt","a",encoding="utf-8") as f:
#     allStr = ""
#     while True:
#         outStr = input("내용입력 : ")
#         if outStr == "":
#             f.write(allStr+"\n")
#             break
#         allStr += (outStr+",")
#         print(allStr)

# 1,홍길동,100,100,100,300,100.0