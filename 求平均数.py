#统计计算.py

from math import sqrt

def getNum() :

# 读入数据

    nums = []
    iNumStr = input("请输入数字，直接按回车退出：")
    while iNumStr != "" :
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字，直接按回车退出：")
    return nums


def mean( numbers ) :

# 计算平均数

    sum = 0
    for i in numbers :
        sum = sum+i
    return sum / len(numbers)

def dev(numbers ,mean) :

# 计算方差

    sdev = 0.0
    for i in numbers :
        sdev = sdev + ( i-mean )**2
    return sqrt( sdev / (len(numbers)-1) )

def median( numbers ):

#求中位数
    
    numbers.sort();
    n = len(numbers)
    if n%2==0 :
        zws = (numbers[ n//2-1 ] + numbers[ n//2 ]) / 2
    elif n%2==1 :
        zws = numbers[ n//2 ]
    return zws

num = getNum()
m = mean(num)
print("平均值为:{},方差为:{},中位数为:{}".format(m, dev(num, m), median(num)))
