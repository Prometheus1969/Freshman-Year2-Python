#鸡兔同笼.py

for i in range(21) :
    for j in range(34) :
        z = 100 - i - j
        if z % 3 == 0 and i*5 + j*3 +z/3 == 100 :
            print("公鸡数为：{},母鸡数为：{},小鸡数为：{}".format(i,j,z))
