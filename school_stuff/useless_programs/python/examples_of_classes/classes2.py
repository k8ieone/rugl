#!/usr/bin/env python

# Class definition
class Container:
    def __init__(self, max_volume):
        self.__max_volume = max_volume
        self.current_volume = 0
        print("Created a container with a volume of", self.__max_volume, "liters.")
    def pridej(self, mnozstvi):
        if self.__max_volume < (self.current_volume + mnozstvi):
            print("You can't add more water to the container than it's maximum volume!")
            print("Filling the entire container...")
            self.current_volume = self.__max_volume
            return 0
        self.current_volume += mnozstvi
        return 0
    def uber(self, mnozstvi):
        if (self.current_volume - mnozstvi) < 0:
            print("Pouring out the entire container...")
            self.current_volume = 0
            return 0
        self.current_volume -= mnozstvi
        return 0

# Object creation
container1 = Container(5)

# Operations with the object
container1.pridej(4)
container1.pridej(2)
container1.uber(5)
container1.uber(1)
print("Current volume of the container is", container1.current_volume, "liters.")
