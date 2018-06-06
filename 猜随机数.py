#猜随机数(一次最多猜五次)

from random import randint

x = eval(input("请输入1到100中的一个数："))
n = randint( 1, 100)
T = 5
while T > 1 :
    if x > n :
        print("猜大了")
    elif x < n  :
        print("猜小了")
    else :
        print("恭喜猜对了")
        break
    T = T - 1
    x = eval(input("请输入1到100中的一个数："))

print()

if T == 1 :
    print("游戏失败")
else :
    print("游戏成功")
