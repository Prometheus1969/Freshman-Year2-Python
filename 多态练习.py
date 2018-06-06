#多态练习.py

class Animal :
    name = "animal"

    def showName(self) :
        print(self.name)

    def bgEat(self) :
        print("eat everything ")

class Sheep(Animal) :
    name = "Sheep"

    def bgEat(self) :
        print("eat Grass")

class Dog(Animal) :
    name = "dog"

    def bgEat(self) :
        print("eat Meet")

dog = Dog()
dog.showName()
dog.bgEat()

sheep = Sheep()
sheep.showName()
sheep.bgEat()
        
        
