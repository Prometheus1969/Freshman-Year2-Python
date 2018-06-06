#水仙花数.py

for i in range(100, 1000, 1) :
    g,s,b = map(int,str(i))
    if g**3 + s**3 + b**3 == i :
        print(i)
