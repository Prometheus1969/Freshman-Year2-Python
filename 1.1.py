def tempconvert(ValueStr) :
    if ValueStr[-1] in ['F','f'] :
        C = (eval(ValueStr[0:-1]) - 32)/1.8
        print("转换后的温度为{:.2f}C".format(C))
    elif ValueStr[-1] in ['C','c'] :
        F = eval(ValueStr[0:-1])*1.8 + 32
        print("转换后的温度为{:.2f}F".format(F))
    else :
        print("输入格式有误")
    TempStr = input("请输入带符号的温度:")
    tempconvert(TempStr)
              
