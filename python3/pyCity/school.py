import exceptions_school

class school:
    def __init__(self, size, active, type, max_students, current_students, max_teachers, current_teachers, focus = None, playground = False, playground_size = None, pool = False):
        self.__size = size
        self.__active = active
        self.__type = type
        self.__max_students = max_students
        self.__current_students = current_students
        self.__max_teachers = max_teachers
        self.__current_teachers = current_teachers
        self.__focus = focus
        self.__playground = playground
        self.__playground_size = playground_size
        self.__pool = pool

    def getSize(self):
        return self.__size

    def getActive(self):
        return self.__active

    def getType(self):
        return self.__type

    def getMax_students(self):
        return self.__max_students

    def getCurrent_students(self):
        return self.__current_students

    def getMax_teachers(self):
        return self.__max_teachers

    def getCurrent_teachers(self):
        return self.__current_teachers

    def getFocus(self):
        return self.__focus

    def getPlayground(self):
        return self.__playground

    def getPlayground_size(self):
        return self.__playground_size

    def getPool(self):
        return self.__pool

    def setStudents(self, students):
        if students <= self.getMax_students():
            self.__current_students = students
        
        elif students > self.getMax_students():
            raise TooMuchStudents("You can't have more students than the maximum.")

        else:
            raise InvalidNumberOfStudents("You have entered invalid number of students") 

    def setTeachers(self, teachers):
        if teachers <= self.getMax_teachers():
            self.__current_teachers = teachers
        
        elif teachers > self.getMax_students():
            raise TooMuchTeachers("You can't have more teachers than the maximum.")

        else:
            raise InvalidNumberOfTeachers("You have entered invalid number of teachers") 

    def CloseSchool(self):
        if self.getActive:
            self.__active = False

        else:
            raise CantCloseSchool("School is already closed")

    def OpenSchool(self):
        if self.getActive:
            raise CantOpenSchool("School is already opened")

        else:
            self.__active = True