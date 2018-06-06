#猜随机数

import random
num = int(random.random()*100)
time = 5
maxnum = 100
while time>0 :
    try:
        x = int(input("请输入猜测的值:"))
    except:
        print("请输入1-100以内的整数")
    if x==num :
        print("恭喜猜对了")
        break
    elif x<num :
        print("对不起，猜小了")
    elif x>num :
        print("对不起，猜大了")
    time = time-1
if time==0 :
    print("Fail")
elif time>0 :
    print("Success")
