#!/usr/bin/env python

# This is an example of working with classes and objects

class Ship:
    aimed = False
    def aim(self):
        if self.aimed == False:
            self.aimed = True
            print("Aimed and ready!")
        elif self.aimed == True:
            print("Ready to fire!")
    def shoot(self):
        if self.aimed == False:
            print("We missed our target!")
            print("You need to aim first!")
        elif self.aimed == True:
            print("We got a hit!")
            self.aimed = False

# Galactica = Ship()
# Galactica.aim()
# Galactica.shoot()

class Kitten:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(self.name, ": ", "Meow!", sep="")
micka = Kitten("Micka")
micka.meow()
mourek = Kitten("Mourek")
mourek.meow()
