#继承多态.py

class Bird:
    wings = 2
    head = 1
    eyes = 2
    def canFly(self) :
        print("this guy can fly")
    def eatWhat(self) :
        print("this guy eat meat")

class Qie(Bird) :
    foot = 2
    def canFly(self) :
        print("can't")

class Eagle(Bird) :
    pass

class main :
    qie = Qie()
    print("{},{},{}".format(qie.wings, qie.eyes, qie.foot))
    qie.canFly()
    qie.eatWhat()

    eagle = Eagle()
    
