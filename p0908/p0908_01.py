# 변수, 함수 포함해서 구현
class Car:
    color = ""
    speed = 0
    tire = 0
    door = 0

    # 생성자 - 생성함수 : car() 선언될때 실행되는 함수
    def __init__(self,color,speed,tire,door):
        self.color = color
        self.speed = speed
        self.tire = tire
        self.door = door

    
    def upSpeed(self):
        self.speed += 10

    def downSpeed(self):
        self.speed -= 10

#-------------------------------
# 클래스를 1개 생성
c = Car() # 객체(인스턴스) 생성 / 4개의 변수, 2개의 함수
c.color = "white"
c.speed = 100
c.tire = 5
c.door = 3
c.upSpeed()
# 클래스 객체선언
c2 = Car("skyblue",200,4,5)
# c2.color = "skyblue"
# c2.speed = 200
# c2.tire = 4
# c2.door = 5
c2.upSpeed()

c3 = Car("gray",300,5,5)
# # gray,50,5,5
# c3.color = "gray"
# c3.speed = 300
# c3.tire = 5
# c3.door = 5
c3.upSpeed()



# c2 = Car()
# c2.upSpeed()
# c.color = "white"
# print("색상 :",c.color)
# print("속도 :",c.speed)

# c.upSpeed()
# print("속도2 :",c.speed)
    