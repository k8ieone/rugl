import random

import Services.firestation
import Services.hospital
import Services.police
import Services.regular_building
import Services.school
import Services.special_building

class City:
    def __init__(self, size, current_citizens, finances, name):
        self.__name = name
        self.__size = size
        self.__finances = finances
        self.__current_citizens = current_citizens

    def __str__(self):
        return "Name of city: %s \n Current citizens: %s \n Size of city: %s \n Current finances: %s" % (self.__name, self.__current_citizens, self.__size, self.__finances)

    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def getFinances(self):
        return self.__finances

    def getCurrent_Citizens(self):
        return self.__current_citizens

def CreatingCity():
    answer = ""
    multiplier = 1
    while True:
        answer = str(input("What difficulty do you wanna take? (Noobie/Standard/Proffeional) "))
        if answer == "Noobie": multiplier = 3; break
        elif answer == "Standard": multiplier = 2; break 
        elif answer == "Proffesional": multiplier = 1; break
        else: print("Please select one of the options!")        

    name = str(input("Enter a name for your city: "))
    
    size = "" 
    while True:
        size = str(input(f"Enter the size of {name} (Small/City/Metropolis): "))
        if size == "Small":
            size = random.randint(500, 3000)
            citizens = random.randint(100, 1000) * multiplier
            buildings = citizens / 3
            finances = citizens * multiplier
            break
        elif size == "City":
            size = random.randint(1000, 8000)
            citizens = random.randint(3000, 100000) * multiplier
            building = citizens / 10
            finances = citizens * multiplier
            break
        elif size == "Metropolis":
            size = random.randint(10000, 60000)
            citizens = random.randint(1000000, 100000000000) * multiplier
            buildings = citizens / 100
            finances = citizens * multiplier
            break
        else:
            print("Please select one of the options!")

    name = City(size, citizens, finances, name)
    return name

city = CreatingCity()
print(city)