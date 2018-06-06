#圆的面积和周长

import math

r = eval(input("请输入半径："))

while r != 0 :
#计算面积和周长

    s = math.pi * r * r
    c = math.pi * 2 * r
    print("当半径为{:-^10.2f}时，圆的面积为{:-^10.2f}，圆的周长为{:-^10.2f}\n".format(r,s,c))
    r = eval(input("请输入半径(输入0时结束)："))
print("结束")
