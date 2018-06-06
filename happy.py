#happy birthday.py

import math

def happy( name ) :
    print("Happy birthday,{}".format(name))

def dup( str , times ) :
    print( str*times )

def sum1( x, y, z) :
    sum = x + y + z
    return sum
def sumave( x, y) :
    sum1 = x + y
    ave = sum1/2
    return sum1,ave

he,pj = sumave(4,8)
print(he)
print(pj)
