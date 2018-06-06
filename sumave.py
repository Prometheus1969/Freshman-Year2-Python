#求和及平均

def sumave( x, y) :
    sum = x + y
    aver = sum/2
    return sum,aver

a,b = eval(input("请输入两个数，用英文逗号隔开："))
sum, aver = sumave( a, b)
print("和为{} ,平均值为{}".format( sum, aver))
