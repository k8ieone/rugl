import exceptions_special_building

class SpecialBuilding:
    def __init__(self, size, active, name, max_tourists, current_tourists, max_employees, current_employees):
        self.__size = size
        self.__active = active
        self.__name = name
        self.__max_tourists = max_tourists
        self.__current_tourists = current_tourists
        self.__max_employees = max_employees
        self.__current_employees = current_employees

    def getSize(self):
        return self.__size

    def getActive(self):
        return self.__active

    def getName(self):
        return self.__name

    def getMax_tourists(self):
        return self.__max_tourists

    def getCurrent_tourists(self):
        return self.__current_tourists

    def getMax_employees(self):
        return self.__max_employees

    def getCurrent_employees(self):
        return self.__current_employees

    def setName(self, name):
        self.__name = name

    def setCurrent_tourists(self, tourists):
        if tourists <= self.getMax_tourists():
            self.__current_tourists = tourists

        elif tourists > self.getMax_tourists:
            raise TooMuchTourists("You can't have more tourists than the maximum")

        elif tourists < 0:
            raise InvalidNumberOfTourists("You have entered invalid number of tourists")

        else:
            raise InvalidNumberOfTourists("You have entered invalid number of tourists")

    def setCurrent_employyes(self, employees):
        if employees <= self.getMax_employees():
            self.__current_employees = employees

        elif employees > self.getMax_employees:
            raise TooMuchEmployees("You can't have more employees than the maximum")

        elif employees < 0:
            raise InvalidNumberOfEmployees("You have entered invalid number of employees")

        else:
            raise InvalidNumberOfEmployees("You have entered invalid number of employees")

    def CloseBuilding(self):
        if self.getActive():
            self.__active = False

        else:
            raise CantCloseBuilding("Building is already closed.")

    def OpenBuilding(self):
        if self.getActive():
            raise CantOpenBuilding("Building is already opened.")

        else:
            self.__active = True