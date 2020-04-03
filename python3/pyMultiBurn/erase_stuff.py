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
    print("\n===== Continuous erase =====")
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
        threadlist.append(threading.Thread(target=erase_drive_thread, args=(drive, mode)))
        threadlist[counter].start()
        counter += 1
    print("pymultiburn : Starting", str(len(drives)), "continuous erase jobs!")
    print("Enter \"c\" to stop.")
    choice = str(input("> "))
    if choice == "c":
        active = False
        print("pymultiburn : Stopping!")
        print("pymultiburn : Waiting for all threads to finish...")
        counter = 0
        for drive in drives:
            threadlist[counter].join()
            counter += 1
        print("pymultiburn : All finished!")
        threadlist = []
        cont_erase_menu()

def erase_drive_thread(drive, mode):
    global active
    print("pymultiburn : Process started!")
    while active is True:
        #subprocess.run(["cdrecord", "-eject", "-force", "dev=/dev/" + drive, "blank=" + mode], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #subprocess.run(["xorriso", "-outdev /dev/" + drive, "-blank force:" + mode, "-eject out"])
        if infoparser.get_status(drive) == 1 or infoparser.get_status(drive) == 2 or infoparser.get_status(drive) == 3:
            print("pymultiburn : Waiting 15 seconds for a disc to be inserted into", drive)
            time.sleep(15)
            pass
        elif infoparser.get_status(drive) == 4:
            erase(drive, mode)
            pass

def add_erase_job_menu():
    print("\n===== Add erase job =====")
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
    # TODO: Warn on error
    # TODO: Eject on error
    print("pymultiburn : Disc in " + drive + " erased!")
