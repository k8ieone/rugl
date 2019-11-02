import exceptions_firestation

class FireStation:

    def __init__(self, active, size, max_employees, current_employees):
        self.__active = active
        self.__size = size
        self.__max_employees = max_employees
        self.__current_employees = current_employees

    def getSize(self):
        return self.__size

    def getActive(self):
        return self.__active

    def getMax_employees(self):
        return self.__max_employees

    def getCurrent_employees(self):
        return self.__current_employees

    def setActive(self, active):
        self.__active = active

    def setCurrent_employees(self, employees):
        if employees <= self.getMax_employees():
            self.__current_employees = employees

        elif employees > self.getMax_employees():
            raise TooMuchEmployees("You can't have more employees than the maximal number of employees.")

        else:
            raise InvalidNumberOfEmployees("You have entered invalid number of employees.")

    def closeFirestation(self):
        if self.getActive():
            self.setActive(False)

        else:
            raise CantCloseFirestation("Firestation is already closed")

    def openFirestation(self):
        if not self.getActive():
            self.setActive(True)

        else:
            raise CantOpenFirestation("Firestation is already opened")
        