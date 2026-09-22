# 일반적인 프로그램
color = ""
speed = 0

def upSpeed():
    global speed
    speed += 10

def downSpeed():
    global speed
    speed -= 10

color = " white"
print("색상 : ",color)
print("속도 : ",speed)

upSpeed()
print("속도2 : ",speed)

#------------------------
# 일반적인 프로그램
color2 = ""
speed2 = 0

def upSpeed2():
    global speed2
    speed2 += 10

def downSpeed2():
    global speed2
    speed2 -= 10

color2 = "white"
print("색상 : ",color2)
print("속도 : ",speed2)

upSpeed2()
print("속도2 : ",speed2)

# ChatGPT 수정보완코드
color = "white"
speed = 0

def upSpeed():
    global speed
    speed += 10

def downSpeed():
    global speed

    if speed >= 10:
        speed -= 10
    else: speed =0

print("생상 : ", color)
print("속도 : ", speed)

upSpeed()
print("속도 : ", speed)

downSpeed()
print("속도 : ", speed)