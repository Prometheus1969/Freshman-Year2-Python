class Myint(int) :
    def __add__( self, other ) :
        return int.__sub__( self , other )

x,y = eval(input("请输入两个数："))
print( Myint(x) + Myint(y) )
