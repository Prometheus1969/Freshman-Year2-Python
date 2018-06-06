#.输出n次字符串.py

def dup( str , times ) :
    print( str*times, end =",")

s = input("请输入字符串:")
n = eval(input("请输入重复次数:"))
dup( s, n)
