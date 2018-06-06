#圆点周长和面积

import math

r = eval(input("请输入半径："))
while r != 0 :
    perimeter = r * 2 * math.pi
    area = math.pi * r * r
    print("面积为 {:-^12.2f} ,周长为 {:-^12.2f} \n".format(area,perimeter))
    r = eval(input("请输入半径(输入0时停止)："))
print("结束")
