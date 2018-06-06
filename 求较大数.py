#求较大值.py

def MAx( a , b ) :
    if a > b :
        return a
    elif b > a :
        return b

a,b = eval(input("请输入要比较大小的两个数，用英文逗号隔开："))
print("较大的数为{}".format( MAx( a, b) ))
