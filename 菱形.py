#菱形.py

try :
    n = eval(input("请输入n："))

    for i in range(n) :
        print((" * " * i).center( n * 3 ))
    for i in range( n, 0, -1) :
        print((" * " * i).center( n * 3 ))
except NameError :
    print("     请输入数字!")
