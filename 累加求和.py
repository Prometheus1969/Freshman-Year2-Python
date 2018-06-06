#累加求和.py

s = eval(input("请输入数值："))

#循环求和

while ( s != 0) :
    i,sum = 0,0

#累加

    while ( i <= s ) :
        sum = sum + i
        i = i + 1
    print("当s为{}时，累加求和为{}\n".format(s,sum))

#结束提示
    
    s = eval(input("请输入数值(输入0时停止)："))
print("结束")
