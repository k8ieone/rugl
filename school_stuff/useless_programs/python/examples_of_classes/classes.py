#!/usr/bin/env python

# This is an example of working with classes and objects

# Here we define the class
class Kitten:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(self.name, ": ", "Meow!", sep="")

# Here we create two objects with different variables
micka = Kitten("Micka")
mourek = Kitten("Mourek")
# Here we call functions inside the objects
micka.meow()
mourek.meow()
