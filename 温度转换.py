#读入温度数值和符号(c 或 f)

temp = input("请输入温度（结束计算请输入N):")

#循环控制，输入N时结束输入

while temp [-1] not in ['N','n'] :
    
#判断输入的是华氏温度还是摄氏温度
    
    if temp [-1] in ['C','c']:
        F = 1.8 * eval( temp[0:-1] )+32
        print("当温度为{}时，华氏温度为{:.2f}F\n".format(temp[0:-1],F))
    elif temp [-1] in ['F','f']:
        C = ( eval(temp[0:-1]) - 32 )/1.8
        print("当温度为{}时，摄氏温度为{:.2f}C\n".format(temp[0:-1],C))
    else:
        print("非有效输入")
    temp = input("请输入温度（结束计算请输入N):")

#结束提示
    
print("结束")
