#小鱼.py

import random

class Fish :

    def __init__(self) :
        self.x = random.randint(1,20)
        self.y = random.randint(1,15)
    def bgSwim(self):
        self.x = self.x + 1
        self.y = self.y - 1
        print("此时的位置为:", self.x,"--", self.y)

fish = Fish()
print("此时的位置为:", fish.x, "--", fish.y)
fish.bgSwim()
