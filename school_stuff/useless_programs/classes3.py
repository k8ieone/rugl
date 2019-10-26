#!/usr/bin/env python

from random import randrange

dices = []
class Dice:
    def __init__(self, number_of_sides, name):
        self.__number_of_sides = number_of_sides
        self.name = name
        dices.append(self.name)
    def throw_dice(self):
        return str(randrange(1, self.__number_of_sides))

dice1 = Dice(6, "dice1")
dice2 = Dice(20, "dice2")

def throw_all_dices():
    for dice in dices:
        print(dice.name(), ":", dice.throw_dice(), sep="")

throw_all_dices()
