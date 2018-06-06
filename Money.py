#Money.py
#读入金额和符号

Money = input("请输入带符号的数值(￥/$):")

#判断符号属于美元还是人民币

if Money[-1] in ["$"] :

#转换并输出
    
    rmb = eval( Money[0:-1] )*6
    print("{}  等于  {:.2f}￥".format(Money,rmb))
elif Money[-1] in ["￥"] :
    dollar = eval( Money[0:-1] )/6
    print("{}  =  {:.2f}$".format(Money,dollar))
else :
    print("输入错误")

#结束提示

print("转换结束")
              
