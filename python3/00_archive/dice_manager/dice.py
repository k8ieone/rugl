#!/usr/bin/env python

# This could be quite useful...

from random import randrange

dice = []
running = True

class Die:
    def __init__(self, number_of_sides, myname):
        self.__number_of_sides = number_of_sides
        self.myname = myname
    def throw_dice(self):
        return str(randrange(1, self.__number_of_sides))

def throw_all_dice():
    for die in dice:
        print(die.myname, ": ", die.throw_dice(), sep="")

while running is True:
    print("")
    player_input = str(input("Enter a command: "))
    if player_input == "c" or "create" in player_input or "Create" in player_input:
        die_nsides = int(input("Enter number of sides of the new die: "))
        die_newname = str(input("Enter a name for the die: "))
        dice.append(Die(die_nsides, die_newname))
        print("Die created")
    elif player_input == "otd" or player_input == "t" or player_input == "throw" or player_input == "Throw":
        player_input = int(input("How many sides should the die have? "))
        print("Threw a ", randrange(1, player_input), "!", sep="")
    elif player_input == "h" or "help" in player_input or "Help" in player_input or "HELP" in player_input:
        print("Available commands:")
        print("create, c                - Creates a die")
        print("delete, d                - Deletes a die")
        print("throw, t, otd            - Throws a \"one-time-die\" (OTD)")
        print("throw_all, throw all, ta - Throws all the dice.")
        print("help, h                  - Prints this help")
        print("exit, e                  - Exits the program")
    elif player_input == "ta" or player_input == "throw_all" or player_input == "throw all" or player_input == "Throw All" or player_input == "THROW ALL" or player_input == "Throw all":
        throw_all_dice()
    elif player_input == "e" or "exit" in player_input or "Exit" in player_input or "EXIT" in player_input:
        running = False
    elif player_input == "d" or "Delete" in player_input or "delete" in player_input:
        print("What die would you like to destroy?")
        player_input = int(input("Enter its number here: "))
        counter = 0
        for die in dice:
            counter += 1
            print(counter, ".", die.myname, sep="")
        dice.pop(player_input - 1)
        print("Destroyed die number ", player_input, sep="")
    else:
        print("Wrong command!")
