# My modules
import mainmenu
import infoparser

# System-wide modules
import os
import time
import sys
import threading

drives = infoparser.list_drives()
active = True

def cont_erase_menu():
    print("All drives will be used for erasing!")
    print("Drive will be ejected after it's done erasing.")
    print("Insert a new disc to erase it.")
    print("------------------------------------")
    print("1: Full")
    print("2: As needed")
    print("3: Fast")
    choice = str(input("> "))
    if choice == "..":
        mainmenu.erase_menu()
    elif choice == "h":
        mainmenu.main_menu()
    elif choice == "q":
        sys.exit()
    elif choice == "1":
        erase_mainthread_cont("all")
    elif choice == "2":
        erase_mainthread_cont("as_needed")
    elif choice == "3":
        erase_mainthread_cont("fast")

def erase_mainthread_cont(mode):
    global drives
    global active
    counter = 0
    threadlist = []
    for drive in drives:
        threadlist.append(threading.Thread(target=erase_drive_cont, args=(drive, mode)))
        threadlist[counter].start()
        counter += 1
    print("Starting " + str(len(drives)) + " continuous erase jobs!")
    print("Enter \"c\" to stop.")
    choice = str(input("> "))
    if choice == "c":
        active = False
        print("Stopping!")
        print("Waiting for all threads to finish...")
        counter = 0
        for drive in drives:
            threadlist[counter].join()
            counter += 1
        print("All finished!")
        threadlist = []
        cont_erase_menu()

def erase_drive_cont(drive, mode):
    global active
    print("Process started!")
    while active is True:
        #subprocess.run(["cdrecord", "-eject", "-force", "dev=/dev/" + drive, "blank=" + mode], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #subprocess.run(["xorriso", "-outdev /dev/" + drive, "-blank force:" + mode, "-eject out"])
        erase(drive, mode)
        time.sleep(10)

def add_erase_job_menu():
    print("Select the drive to be used:")
    global drives
    counter = 0
    for drive in drives:
        counter += 1
        print(str(counter) + ": " + drive)
    choice = str(input("> "))
    if choice == "..":
        mainmenu.erase_menu()
    elif choice == "h":
        mainmenu.main_menu()
    elif choice == "q":
        sys.exit()
    else:
        drive = drives[int(choice) - 1]
        print("1: Full")
        print("2: As needed")
        print("3: Fast")
        choice = str(input("> "))
        if choice == "..":
            add_erase_job_menu()
        elif choice == "h":
            mainmenu.main_menu()
        elif choice == "q":
            sys.exit()
        elif choice == "1":
            erase(drive, "all")
            # TODO: Start the job in a new thread so that one can add multiple jobs
            add_erase_job_menu()
        elif choice == "2":
            erase(drive, "as_needed")
            # TODO: same as above ^^^^^
            add_erase_job_menu()
        elif choice == "3":
            erase(drive, "fast")
            # TODO: same as above ^^^^^
            add_erase_job_menu()

def erase(drive, mode):
    command = "xorriso -outdev /dev/" + drive + " -blank force:" + mode + " -eject out"
    # TODO: Use subprocess.run instad of os.system
    # TODO: Redirect the output to a log if run as a single job
    os.system(command)
    # TODO: Make sure the disc was actually erased (xorriso didn't encounter an error)
    print("Disc in " + drive + " erased!")
