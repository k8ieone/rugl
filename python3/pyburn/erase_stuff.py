import mainmenu
import infoparser

import subprocess
import time
import sys
import multiprocessing

drives = infoparser.list_drives()
active = True

def cont_erase_menu():
    print("All drives will be used for erasing!")
    print("Drive will be ejected after it's done erasing.")
    print("Insert a new disc to erase it.")
    print("------------------------------------")
    print("1: Full format")
    print("2. Quick format")
    choice = str(input("> "))
    if choice == "..":
        mainmenu.erase_menu()
    elif choice == "h":
        mainmenu.main_menu()
    elif choice == "q":
        sys.exit()
    elif choice == "1":
        erase_mainthread("all")
    elif choice == "2":
        erase_mainthread("fast")

def erase_mainthread(mode):
    global drives
    global active
    counter = 0
    processlist = []
    for drive in drives:
        processlist.append(multiprocessing.Process(target=erase_drive, args=(drive, mode)))
        processlist[counter].start()
        counter += 1
    print("Starting " + str(len(drives)) + " continuous erase jobs!")
    print("Enter \"c\" to stop.")
    choice = str(input("> "))
    if choice == "c":
        active = False
        print("Stopping!")
        print("All finished!")
        cont_erase_menu()
def erase_drive(drive, mode):
    global active
    print("Process started!")
    while active is True:
        subprocess.run(["cdrecord", "-eject", "dev=/dev/" + drive, "blank=" + mode], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(10)

def add_erase_job_menu():
    pass
