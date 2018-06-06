#数字交换.py

x = input("请输入两个数字:")
a,b = map( int , x.split() )
if ( a < b ) :
    a,b = b,a
print("两个数字为{},{}".format(a,b))
