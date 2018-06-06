
def Name( name ) :
    print("Happy birthday, {}!\n".format(name))

def Aver( x, y ) :
    sum = x + y
    aver = sum/2
    return sum, aver

name = input("请输入姓名：")
Name(name)
x,y = eval(input("请输入x和y:"))
he, pj = Aver(x,y)
print("求和为 {} ,平均值为 {} ".format(he,pj))
