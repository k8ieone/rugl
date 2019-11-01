#!/usr/bin/env python

class Human:
    def __init__(self, name):
        self.__name = name
        self.__tiredness = 0
    def __str__(self):
        return "My name is {0}, my tiredness level is {1}".format(self.__name, self.__tiredness)
    def run(self, distance):
        if self.__tiredness + distance >= 20:
            print("Tiredness would be more than 20!")
            print("Maxing out tiredness")
            self.__tiredness = 20
        else:
            self.__tiredness += distance
    def rest(self, time):
        if self.__tiredness - time * 10 <= 0:
            print("Tiredness would be less than 0!")
            print("Making it 0")
            self.__tiredness = 0
        else:
            self.__tiredness -= time * 10

human1 = Human("Honza")
human1.run(21)
human1.rest(1)
print(human1)
