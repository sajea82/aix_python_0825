class Student:
    def __init__(self,*args):
        if len(args) == 5:
            self.no = args[0]
            self.name = args[1]
            self.kor = args[2]
            self.eng = args[3]
            self.math = args[4]
            self.total = self.kot+self.eng+self.math
            self.avg = self.total

        elif len(args) == 8: