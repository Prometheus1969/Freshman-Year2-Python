class Dog:
    limb = 4

    def setName(self, name ):
        self.name = name
    def eat(self):
        print("{} Eating Meat is {} cm long".format(self.name,self.long))

    def __init__(self, long ):
        self.long = long

long = eval(input("请输入长度："))
dog1 = Dog(long)
name = input("请输入名称：")
dog1.setName(name)
dog1.eat()

