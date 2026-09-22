import os
# r - 읽기, w - 쓰기, a - 이어쓰기
# 없는 폴더에 파일저장시 에러
fname = input("저장할 파일이름을 입력하세요(파일명)>> ")

if not os.path.exists("common"): # 폴더가 있는지 확인
    os.makedirs("common") # 폴더를 생성해줌.

with open("common/+fname","w",encoding="utf-8") as f:
    while True:
        outStr = input("내용입력 : ")
        if outStr == "": break
        f.write(outStr+"\n") # \n 꼭입력

print("파일내용이 저장되었습니다.")