#!/usr/bin/env python

# Class definition
class Nadoba:
    def __init__(self, max_obsah):
        self.__max_obsah = max_obsah
        self.obsah = 0
        print("Vytvořena nádoba s maximálním obsahem", self.__max_obsah, "litrů.")
    def pridej(self, mnozstvi):
        if self.__max_obsah < (self.obsah + mnozstvi):
            print("Do nádoby nelze přidat větší množství vody, než její objem!")
            print("Doplňuji celou nádobu...")
            self.obsah = self.__max_obsah
            return 0
        else:
            self.obsah += mnozstvi
            return 0
    def uber(self, mnozstvi):
        if (self.obsah - mnozstvi) < 0:
            print("Obsah by se rovnal nule, vylévám celou nádobu...")
            self.obsah = 0
            return 0
        else:
            self.obsah -= mnozstvi
            return 0

# Object creation
nadoba1 = Nadoba(5)

# Operations with the object
nadoba1.pridej(4)
nadoba1.pridej(2)
nadoba1.uber(5)
nadoba1.uber(1)
print("Obsah nádoby je nyní", nadoba1.obsah, "litrů.")
