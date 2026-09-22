class Student:
    def __init__(self,no,name,kor,eng,math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = (kor+eng+math)/3

    def sum(self):
        self.sum = self.kor + self.eng + self.math

    def avg(self):
        self.avg = self.sum/3

    def print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,f"{self.avg:.2f}",sep="\t")

stuLst = []
s = Student(1,"홍길동",100,100,100)
s.print()