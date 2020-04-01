import os
import sys
import time
import random
import randomquote
authorization = False
name = ""
number_previous = 0

def Quotes():
    print(randomquote.GetQuote())

def Negace():
    global authorization
    authorization = False
    
def Login():
    global authorization
    global name
    pokus = 3
    while pokus > 0:

        print("Počet zbývajících pokusů: ", pokus)
        name_input = str(input("Zadej přihlašovací jméno: "))
        password_input = str(input("Zadej svoje heslo: "))
        exist = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input)
        if exist:
            login_file = open(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input, "r")
            login_input = login_file.read().splitlines()
            name = login_input[0]
            password = login_input[1]
            permision = login_input[2]
    
            if name == name_input and password == password_input:
                print("Přihlašování..")
                time.sleep(1)
                print("Ověřování atomové struktury vašeho mozku..")
                time.sleep(1)
                print("Skenování vašich chodidel..")
                time.sleep(1.5)
                print("Přihlášení bylo úspěšné")
                pokus = 0
                authorization = True
        
            else:
                print("Skenování spodní strany očních víček..")
                time.sleep(1)
                print("Špatné přihlašovací heslo")
                pokus = pokus - 1
                
        else:
            print("Prohledávání svalových vláken v okolí krku..")
            time.sleep(1)
            print("Špatné přihlašovací jméno")
            pokus = pokus - 1      
            
    if authorization:
        Negace()
        
    else:
        print("Došly ti pokusy")
        exit()

def Log_out():
    global name 
    confirmation = input("Vážně se chcete odhlásit? (Y/N) ")
    if confirmation == "Y" or confirmation == "y":
        name = ""
        print("Farewell, old friend..")
        time.sleep(1)
        Quotes()
        time.sleep(5)
        print("Uživatel odhlášen")
        print("Pro další akce se musíte přihlásit")
        Login()
        
    else:
        print("Akce zrušena")

def Authorization():
    global authorization
    pokus = 3
    
    while pokus > 0:
        print("Počet zbývajících pokusů: ", pokus)
        name_input = str(input("Zadej přihlašovací jméno: "))
        password_input = str(input("Zadej svoje heslo: "))
        exist = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input)
        
        if exist:
            login_file = open(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input, "r")
            login_input = login_file.read().splitlines()
            name = login_input[0]
            password = login_input[1]
            permision = login_input[2]
    
            if name == name_input and password == password_input:
                print("Sken celého těla..")
                time.sleep(2)
                print("Ověření bylo úspěšné")
                pokus = 0
                authorization = True
        
            else:
                print("Kontrola hladiny kyslíku v krvi..")
                time.sleep(1)
                print("Špatné přihlašovací údaje")
                pokus = pokus - 1
                
        else:
            print("Měření světového rekordu v zapomínání..")
            time.sleep(.500)
            print("Škoda, nejste nejrychlejší..")
            time.sleep(.500)
            print("Špatné přihlašovací údaje")
            pokus = pokus - 1
            
    if authorization:
        pass
        
    else:
        print("Došly ti pokusy")
        exit()
        
def Root_Authorization():
    global authorization
    global name
    pokus = 3
    while pokus > 0:
        #print("Počet zbývajících pokusů: ", pokus)
        name_input = name
        password_input = str(input("Zadej svoje heslo: "))
        exist = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input)
        
        if exist:
            login_file = open(os.path.dirname(os.path.abspath(__file__)) + "/" + name_input, "r")
            login_input = login_file.read().splitlines()
            name = login_input[0]
            password = login_input[1]
            permision = login_input[2]
    
            if name == name_input and password == password_input and permision == "root":
                print("Měření úbytku vlasů za poslední 2 vteřiny..")
                time.sleep(1)
                print("Měření délky prstů..")
                time.sleep(1)
                print("Ověření bylo úspěšné")
                pokus = 0
                authorization = True
        
            elif name == name_input and password == password_input and permision != "root":
                print("Probíhá sken obličeje..")
                time.sleep(1)
                print("Měření rozteče očí..")
                time.sleep(1)
                print("Nedostatečné permise")
                pokus = 0
                
            else:
                print("Sken nehtových lůžek..")
                time.sleep(1)
                print("Sken oční bulvy..")
                time.sleep(1)
                print("Špatné přihlašovací údaje")
                pokus = 0
                
        else:
            print("Špatné přihlašovací údaje")
            pokus = pokus - 1
            
def Registration():
    if not os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/"):
        name = str(input("Zadej svoje přihlašovací jméno pro vytvoření účtu: "))
        password = str(input("Zadej svoje heslo pro vytvoření účtu: "))
        permission = "user"
        login_file = open(os.path.dirname(os.path.abspath(__file__)) + "/" + name, "w")
        login_file.write(name + "\n")
        login_file.write(password + "\n")
        login_file.write(permission + "\n")
        login_file.close()
        print("Ověřuji zadané údaje..")
        time.sleep(1)
        print("Hledám v trestním rejstříku..")
        time.sleep(1)
        print("Skenuji sovětským satelitem..")
        time.sleep(1)
        print("Prověřuji vaše atomové složení..")
        time.sleep(1)
        print("Vytvářím účet..")     
        
def Create():
    global authorization
    Negace()
    Root_Authorization()
    
    if authorization:        
        name = str(input("Zadej svoje přihlašovací jméno pro vytvoření účtu: "))
        password = str(input("Zadej svoje heslo pro vytvoření účtu: "))
        permission = str(input("Zadej permise pro účet (root/user): "))
        
        try:
            login_file = open(os.path.dirname(os.path.abspath(__file__)) + name, "w")
            login_file.write(name + "\n")
            login_file.write(password + "\n")
            login_file.write(permission + "\n")
            login_file.close()
            print("Ověřuji zadané údaje..")
            time.sleep(1)
            print("Hledám v trestním rejstříku..")
            time.sleep(1)
            print("Skenuji sovětským satelitem..")
            time.sleep(1)
            print("Prověřuji vaše atomové složení..")
            time.sleep(1)
            print("Vytvářím účet..")
            time.sleep(1)
            print("Ověření údajů: ")
            Negace()
            Authorization()
            
        except FileExistsError:
            print("Naše intergalaktické sdružení si nemyslí, že tomu rozumí..")
            time.sleep(1)
            print("Neplatné zadání")
        
    else:
        pass
    
def Delete():
    global authorization
    Negace()
    Root_Authorization()
    if authorization:  
        name = str(input("Zadejte název účtu, který chcete smazat: "))
        confirmation = str(input("Jste si jistí, že chcete smazat účet "+ name + "? (Y/N) "))
        
        if confirmation == "Y" or confirmation == "y":
            exist = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/" + name) 
            if exist:
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "/" + name)
                print("Hledání návazností v paralelních vesmírech..")
                time.sleep(1)
                print("Probíhá vymazávání účtu..")
                time.sleep(1)
                print("Odstranění úspěšné")
            
            else:
                print("Prohledávání mezigalaktické databáze..")
                time.sleep(1)
                print("Zvolený účet neexistuje")
            
        else:
            print("Když myslíte..")
            time.sleep(1)
            print("Akce zrušena")
            
    else:
        pass
    

def Help():
    print("Načítání nápovědy z intergalaktické stanice..")
    time.sleep(1)
    print("Pro vytvoření účtu zadejte --c ")
    print("Pro smazání účtu zadejte --d ")
    print("Pro odhlášení zadejte --lo ")
    print("Pro vypnutí programu zadejte --e ")
    print("Pro vystoupení z programu zadejte --b ")
    print("Pro zobrazení náhodného citátu zadejte --q")
    print("Pro zobrazení -loga- zadejte --logo")
    print("Pro zobrazení této nápovědy zadejte --h ")
    
    
def Exit():
    confirmation = input("Vážně chcete odejít? (Y/N) ")
    
    if confirmation == "Y" or confirmation == "y":    
        print("Dobře, s touto možností jsem nepočítal..")
        time.sleep(1)
        Quotes()
        time.sleep(5)
        print("Ukončování programu..")
        time.sleep(3)
        exit()
        
    else:
        print("Nejste vy žena?..")
        time.sleep(1)
        print("Akce zrušena")                 
        
def Input():
    while True:        
        text = input()
        if text == "c":
            Create()
            Negace()
            
        elif text == "d":
            Delete()
            Negace()
            
        elif text == "lo":        
            Log_out()
               
        elif text == "e":
            Exit()
            
        elif text == "b":
            break
        
        elif text == "q":
            Quotes()
        
        elif text == "h":
            Help()
            
        elif text == "logo":
            screen()
            
        else:
            print("Neznámý příkaz -- pro nápovědu zadejte -h- ")
               
def screen():
    print("██    ▐█▀▀█▌ ▐█▀▀▀  ▐██  ██▄  █▌")
    print("██    ▐█▄ █▌ ▐█ ▀█▌  █▌  ▐█ █ █ ")
    print("██▄▄█ ▐██▄█▌ ▐██▄█▌ ▐██  ██  ██▌")
    print("")
    print("         █▀█▀█ ▐█▀▀█▌")    
    print("           █   ▐█▄ █▌")   
    print("          ▄█▄  ▐██▄█▌")
    print("")
    print("   ╔═╦╗╔═╗╔╦═╦╗╔╗╔╗╔═╗╔═╗╔═╗")
    print("   ║║║║║║║║║║║║║╚╝║║╦╝║╬║║╦╝")
    print("   ║║║║║║║║║║║║║╔╗║║╩╗║╗╣║╩╗")
    print("   ╚╩═╝╚═╝╚═╩═╝╚╝╚╝╚═╝╚╩╝╚═╝")
    
screen()
Registration()
Login()
Negace()
Input()
