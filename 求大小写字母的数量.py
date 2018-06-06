#求大小写字母的数量.py

def Aa( str ) :
    n1 = 0
    n2 = 0
    for ch in str :
        if ch <= "z" and ch>= "a" :
            n2 = n2 + 1
        elif ch >= "A" and ch <= "Z" :
            n1 = n1 + 1
    return n1, n2

str = input("请输入一个字符串：")
n1, n2 = Aa(str)
print("大写字母有 {} 个".format(n1))
print("小写字母有 {} 个".format(n2))
