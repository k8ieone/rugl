import exceptions_regular_building

class RegularBuilding:
    def __init__(self, size, type, max_residents, current_residents):
        self.__size = size
        self.__type = type
        self.__max_residents = max_residents
        self.__current_residents = current_residents

    def getSite(self):
        return self.__size

    def getType(self):
        return self.__type

    def getMax_residents(self):
        return self.__max_residents

    def getCurrent_residents(self):
        return self.__current_residents

    def setCurrent_residents(self, residents):
        if residents <= self.getMax_residents():
            self.__current_residents = residents

        elif residents < 0:
            raise InvalidNumberOfResidents("You have entered invalid number of residents")

        else:
            raise InvalidNumberOfResidents("You have entered invalid number of residents")