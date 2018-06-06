#矩形练习.py

class Jx :

    def __init__(self, height=1, long=1) :
        self.height = height
        self.long = long

    def setLong(self, long) :
        self.long = long

    def setHeight(self, height) :
        self.height = height

    def getArea(self) :
        return self.height * self.long

x,y = eval(input("请输入长和宽，用逗号分隔："))
a = Jx()
a.setLong(x)
a.setHeight(y)
area = a.getArea()
print(area)
