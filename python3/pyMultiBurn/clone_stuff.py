import mainmenu
import infoparser

import os
import time
import threading
# TODO: the entire thing

drives = infoparser.list_drives()
active = True

def cont_clone_menu():
    global drives
    print("Enter where to save the resulting ISOs")
    location = input("> ")
    if location == "h":
        mainmenu.main_menu()
    elif location == "..":
        mainmenu.clone_menu()
    elif os.path.isdir(location) is False:
        print("Directory doesn't exist or you don't have read permission.")
        cont_clone_menu()
    elif os.path.isdir(location) is True:
        clone_mainthread(location)
    # The filename will be determined by the threads
    # the thread will check the volume name and check if that file exists
    # if it exists, a number will be added to the filename
    # this keeps happening until a filename that doesn't exist is determined

def clone_mainthread(outpath):
    global drives
    global active
    counter = 0
    threadlist = []
    print("pymultiburn : Starting", str(len(drives)), "cloning threads")
    for drive in drives:
        threadlist.append(threading.Thread(target=clone_drive_thread, args=(drive, outpath)))
        threadlist[counter].start()
        counter += 1
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
        cont_clone_menu()

# This is the function the threads are running
def clone_drive_thread(drive, outpath):
    global active
    print("pymultiburn : Process started!")
    while active is True:
        if infoparser.get_status(drive) == 1 or infoparser.get_status(drive) == 2 or infoparser.get_status(drive) == 3:
            print("pymultiburn : Waiting 15 seconds for a disc to be inserted into", drive)
            time.sleep(15)
            pass
        elif infoparser.get_status(drive) == 4:
            clone(drive, outpath)
            pass

def add_clone_job_menu():
    pass

# This determines the filename and starts the cloning job
# TODO: Somewhere in this function is a bug. Each time a disc is copied, a new filename is appended to the previous one. (filename = filename + new)
def clone(drive, outpath):
    outfile = outpath + "/" + infoparser.get_volname(drive)
    outfile = ''.join(outfile.split())
    outfile1 = outfile + ".iso"
    counter = 0
    if os.path.isfile(outfile + ".iso") is True:
        outfile1 = outfile + str(counter) + ".iso"
        while os.path.isfile(outfile1) is True:
            counter += 1
            outfile1 = outfile + str(counter) + ".iso"
    if " " in outfile1:
        outfile1 = outfile1.replace(" ", "_")
    command = "dd if=/dev/" + drive + " of=" + outfile1 + " status=progress " + "bs=" + infoparser.get_sector_size(drive)
    print(outfile1)
    os.system(command)
    command = "eject " + drive
    os.system(command)
