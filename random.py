#random.py

from random import random
from math import sqrt
from time import clock
DARTS = 10000000
hits = 0.0
clock()
for i in range( 1, DARTS+1 ) :
    x , y = random() , random()
    dist = sqrt( x*x + y*y )
    if dist <= 1 :
        hits = hits + 1
pi = 4 * ( hits / DARTS )
print("Pi的值为 {}.".format(pi))
print("运行时间为： {:5.5} s".format(clock()))
