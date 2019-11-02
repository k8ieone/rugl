import random

import Services.firestation
import Services.hospital
import Services.police
import Services.regular_building
import Services.school
import Services.special_building

class City:
    def __init__(self, size, citizens, current_citizens, finances, name):
        self.__name = name
        self.__size = size
        self.__citizens = citizens
        self.__finances = finances
        self.__current_citizens = current_citizens

    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def getCitizens(self):
        return self.__citizens

    def getFinances(self):
        return self.__finances

    def getCurrent_Citizens(self):
        return self.__current_citizens

def CreatingCity():
    answer = ""
    multiplier = 1
    while answer != "Noobie" or answer != "Standard" or answer != "Proffesional":
        answer = str(input("What difficulty do you wanna take? (Noobie/Standard/Professional)"))
        if answer != "Noobie" or answer != "Standard answer" or answer != "Proffesional":
            print("Please choose one of the options.")

    if answer == "Noobie": multiplier = 1
    elif answer == "Standard": multiplier = 2
    elif answer == "Proffesional": multiplier = 3

    name = str(input("Enter a name for your city: "))
    
    size = "" 
    while size != "Small" or size != "City" or size != "Metropolis":
     size = str(input(f"Enter the size of {name} (Small/City/Metropolis): "))

     if size != "Small" or size != "City" or size != "Metropolis":
         print("Please choose one of the options.")

    if size == "Small":
        size = random.randint(500, 500)
        citizens = random.randint(100, 1000) * multiplier
    if size == "City":
        size = random.randint(1000, 1000)
        citizens = random.randint(3000, 100000) * multiplier
    if size == "Metropolis":
        size = random.randint(10000, 10000)
        citizens = random.randint(1000000, 100000000000) * multiplier

