import exceptions_police

class Police:
    
    def __init__(self, size, active, max_employees, jail_size):
        self.__size = size
        self.__active = active
        self.__max_employees = max_employees
        self.__jail_size = jail_size

    
    def getSize(self):
        return self.__size

    def getActive(self):
        return self.__active

    def getMax_employees(self):
        return self.__max_employees

    def getJail_size(self):
        return self.__jail_size

    def setActive(self, active):
        self.__active = active

    def closePolice(self):
        if self.getActive():
            self.setActive(False)

        else:
            raise CantClosePolice("Police is already closed")

    def openPolice(self):
        if not self.getActive():
            self.setActive(True)

        else:
            raise CantOpenPolice("Police is already opened")

    def setCurrent_employees(self, employees):
        if employees <= self.getMax_employees():
            self.__current_employees = employees

        elif employees > self.getMax_employees():
            raise TooMuchEmployees("You can't have more employees than the maximal number of employees.")

        else:
            raise InvalidNumberOfEmployees("You have entered invalid number of employees.")