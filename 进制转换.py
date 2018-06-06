#进制转换.py
#读入数字1

num1 = input("请输入要转换的十进制数字：")
num1 = eval(num1)

#进制转换

print("{}的八进制数是{},十六进制数是{}".format(num1,oct(num1),hex(num1)))

#读入数字2

num2 = eval(input("请输入数字："))

#输出
print("num1 // num2 = {}".format(num1//num2))
print("divmod( num1 , num2 ) = {}".format(divmod(num1,num2)))
