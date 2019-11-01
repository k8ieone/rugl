import os

authorization = False

def input():

    requirement = str(input())
    
    if requirement == "-h":
        print("To log in type: -l", end = "")
        print("To log out type: -lo", end = "")
        print("To see installed modules type: -m", end = "")
        print("To register or create new user (admins only): -r", end = "")
        print(" ")
        print("===================================")   

    elif requirement == "-l":
        authorization = login()

    elif requirement == "-lo":
        pass

    elif requirement == "-m":
        pass

    elif requirement == "-r":
        pass

def login():
    name = str(input("Enter your name: "))

    if not os.path.exists("/logins/" + name):
        print("Wrong name or you doesn't have an account yet")

    else: 
        password = str(input("Enter your password: "))
        open("/logins/" + name, "r")
        acc = list("/logins/" + name)

        if acc[0] == name and acc[1] == password:
            print("You have sucesffully loged in")

            return True, bool(acc[2])
            

        else: 
            print("You have entered wrond password")

            return False 

def register(authorization):
    if len(os.listdir("/logins")) == 0:
        name = str(input("Enter your name: "))
        password = str(input("Enter your password: "))
        acc = open("/logins/" + name, "w+")
        acc.write(name + "\n")
        acc.write(password + "\n")
        acc.write("True \n")

        print("You have now created an admin account!")

