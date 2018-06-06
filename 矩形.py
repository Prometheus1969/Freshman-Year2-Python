class JuXing :

    def setData( self, long, height ) :
        self.long = long
        self.height = height

    def getArea( self ) :
        return self.long*self.height

a = JuXing()
x,y = eval(input("请输入两个数字："))
a.setData( x, y )
print(a.getArea())
