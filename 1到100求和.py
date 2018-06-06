#1到100求和.py

n = eval(input("请输入n的值："))
x = range( 1, n+1 ,1 )
sum = 0
for i in x:
    sum = sum + i
print(sum)
