
# 파일복사하기
import os


rf = open("c:/aaa/1.jpg","rb") # 1 byte
wf = open("c:/aaa2/2.jpg","wb") # b를 붙이면 파일

while True:
    fdata  = rf.read(1)
    if not fdata: break
    wf.write(fdata)

rf.close()
wf.close()

print("이미지 파일이 복사되었습니다.")