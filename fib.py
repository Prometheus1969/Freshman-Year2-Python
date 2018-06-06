#Fib.py

def Fib( n ) :
    '''输入一个数
       输出n之前的斐波那契数'''
    a , b = 1 , 1
    while a < n :
        print(a,end=" ")
        a , b = b , a+b
    print()

n = eval(input("请输入n："))
Fib(n)
