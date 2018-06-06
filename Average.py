#Average.py
#读入a和b的值

a = input("请输入a = ")
b = input("请输入b = ")

#将读入的a和b由字符串转换成数字，并计算平均值

ave = (eval(a)+eval(b))/2

#输入平均值

print("a和b的平均值为{:.2f}".format(ave))
if a==b:
    print("dasds")
else:
    print("xxxxx")
