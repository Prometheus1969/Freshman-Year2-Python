#可变数量参数.py

def abc( a , *b ) :
    for i in b :
        a = a + i
    return a

sum = abc(1,2,3,4,5,6,7)
print(sum)
