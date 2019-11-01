import exeptions_hospital

class Hospital:

    def __init__(self, active, size, max_patients, max_employees, pharmacy, pharmacy_size = None, pharmacy_active = False):
        self.__size = size
        self.__active = active
        self.__max_patients = max_patients
        self.__max_employees = max_employees
        self.__pharmacy = pharmacy
        self.__current_patients = 0
        self.__pharmacy_size = pharmacy_size
        self.__pharmacy_active = pharmacy_active


    def getSize(self):
        return __size

    def getActive(self):
        return __active

    def getMax_patients(self):
        return __max_patients

    def getMax_employees(self):
        return __max_employees

    def getPharmacy(self):
        return __pharmacy

    def getPharmacy_active(self):
        return __pharmacy_active

    def getCurrent_patients(self):
        return __current_patients

    def setCurrent_patients(self, current_patients):
        self.__current_patients = current_patients

    def setActive(self, active):
        self.__active = active

    def setPharmacy_active(self, active):
        self.__pharmacy_active = active

    
    def closeHospital(self):
        if self.getActive:
            self.setActive(False)

        else:
            raise CantCloseHospital

    def openHospital(self):
        if not self.getActive:
            self.setActive(True)

        else:
            raise CantOpenHospital
        
    def closePharmacy(self):
        if self.getPharmacy and self.getPharmacy_active:
            self.setPharmacy_active(False)

        elif not self.getPharmacy:
            raise DoesntHavePharmacy

        else:
            raise CantClosePharmacy

    def openPharmacy(self):
        if self.getPharmacy and not self.getPharmacy_active:
            self.setPharmacy_active(True)

        elif not self.getPharmacy:
            raise DoesntHavePharmacy

        else:
            raise CantOpenPharmacy


