#iuthe.py

from math import sqrt

def getMax( x, y ):
    if x>y :
        return x
    else:
        return y
    
def getNum() :
    nums = []
    NumStr = input("请输入数字，直接按回车时结束：")
    while NumStr != "" :
        nums.append(eval(NumStr))
        NumStr = input("请输入数字，直接按回车时结束：")
    return nums

def mean( nums ) :
    sum = 0
    for i in nums :
        sum = sum + i
    return sum / len(nums)

def dev( nums, aver ) :
    sum = 0
    for i in nums :
        sum = sum + (i-aver)**2
    return sqrt( sum / (len(nums)-1))

nums = getNum()
sum = mean( nums )
aaa = dev( nums, sum )
print("平均数为{:-^12.3f}\nsdev为  {:-^12.3f}".format(sum, aaa))
