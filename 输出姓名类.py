class Person:

    def __init__(self, name, height, animal, weight):
        self.name = name
        self.height = height
        self.animal = animal
        self.weight = weight

    def getName(self):
        if self.animal == "狗":
            print("{}, happy dog!".format(self.name))

        else :
            print("{}".format(self.name))

name = input("请输入姓名:")
height = eval(input("请输入身高:"))
animal = input("请输入属相:")
weight = eval(input("请输入体重:"))
person = Person(name, height, animal, weight)
person.getName()
print("身高：{}，体重：{}".format(person.height, person.weight))
