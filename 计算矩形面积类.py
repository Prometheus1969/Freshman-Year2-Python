class Area :

    def __init__(self, long, height) :
        self.long = long
        self.height = height
    def getArea(self):
        self.area = self.long * self.height
        return self.area

x,y = eval(input("请输入长和宽:"))
jack = Area(x,y)
area = jack.getArea()
print(area)
        
