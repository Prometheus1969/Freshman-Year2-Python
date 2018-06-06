#类的练习.py

class Person :

    height = 180
    name = "Jack"
    eyes = 2

    def bgSpeak(self) :
        print("I can speak")

    def __init__(self, weight=3) :
        self.weight = weight
        print("ok")


class Father(Person) :

    def getName(self) :
        print(self.name)
        
