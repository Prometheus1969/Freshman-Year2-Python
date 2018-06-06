#继承的练习.py

class Parent :
    
    house = 2
    money = 10000

    def printinfo(self) :
        print("现在调用父类的方法")

class Child(Parent) :

    def printinfo(self):
        print("现在调用子类的方法")

a = Parent()
b = Child()

print("a : {},{}".format(a.house, a.money))
a.printinfo()
print("b : {},{}".format(b.house, b.money))
b.printinfo()
