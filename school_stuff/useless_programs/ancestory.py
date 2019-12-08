#!/usr/bin/env python

class Person:
    def __init__(self, myname, ancestor_male=None, ancestor_female=None):
        self.__myname = myname
        self.__ancestor_male = ancestor_male
        self.__ancestor_female = ancestor_female
    
    def get_name(self):
        return self.__myname

    def get_male_ancestor(self):
        return self.__ancestor_male

    def get_female_ancestor(self):
        return self.__ancestor_female
    
    def __str__(self):
        return self.__myname    

# Really weird solution I somehow came up with...
def male_male(person):
    left = True
    while left is True:
        if person.get_male_ancestor() != None:
            print(person.get_male_ancestor())
            person = person.get_male_ancestor()
        else:
            left = False

def male_female(person):
    left = True
    while left is True:
        person = person.get_female_ancestor()
        if person.get_female_ancestor() != None:
            print(person.get_male_ancestor())
        else:
            left = False

def female_male(person):
    left = True
    while left is True:
        if person.get_male_ancestor() != None:
            print(person.get_female_ancestor())
            person = person.get_male_ancestor()
        else:
            left = False

def female_female(person):
    left = True
    while left is True:
        person = person.get_female_ancestor()
        if person.get_female_ancestor() != None:
            print(person.get_female_ancestor())
        else:
            left = False

def print_all_ancestors_old(person):
    print("[V1] Ancestory for ", person.get_name(), ":", sep="")
    male_male(person)
    female_male(person)
    male_female(person)
    female_female(person)

# The (much) better solution:
def print_male_ancestors(person):
    male_ancestors_left = True
    print(person.get_name())
    print(person.get_male_ancestor())
    person = person.get_male_ancestor()
    while male_ancestors_left is True:
        if person.get_male_ancestor() != None:
            print(person.get_male_ancestor())
            print(person.get_female_ancestor())
            person = person.get_male_ancestor()
        else:
            male_ancestors_left = False

def print_female_ancestors(person):
    female_ancestors_left = True
    print(person.get_female_ancestor())
    person = person.get_female_ancestor()
    while female_ancestors_left is True:
        if person.get_female_ancestor() != None:
            print(person.get_male_ancestor())
            print(person.get_female_ancestor())
            person = person.get_female_ancestor()
        else:
            female_ancestors_left = False

def print_all_ancestors(person):
    print("[V2] Printing ancestors of", person.get_name())
    print_male_ancestors(person)
    print_female_ancestors(person)

abraham = Person("Abraham Simpson")
penelope = Person("Penelope Olsen")

herb = Person("Herb Powers", abraham, penelope)
homer = Person("Homer Simpson", abraham, penelope)

pan = Person("Pan Bouvier")
jackie = Person("Jackie Bouvier")

marge = Person("Marge Bouvier", pan, jackie)
selma = Person("Selma Bouvier", pan, jackie)

bart = Person("Bart Simpson", homer, marge)

print("Ancestory version 1 (weirdly organised output):")
print_all_ancestors_old(bart)
print_all_ancestors_old(homer)
print("")
print("Ancestory version 2 (correctly organised output):")
print_all_ancestors(bart)
print_all_ancestors(homer)
