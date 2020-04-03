import erase_stuff
import clone_stuff

import sys
# TODO: Make the separation between menus and output a little better (use =====)
def main_menu():
    print("\n===== Main menu =====")
    print("1: Clone as ISO")
    print("2: Erase rewriteable (only CD-RW and DVD-RW is supported now!)")
    choice = str(input("> "))
    if choice == "..":
        main_menu()
    elif choice == "h":
        main_menu()
    elif choice == "q":
        sys.exit()
    elif choice == "1":
        clone_menu()
    elif choice == "2":
        erase_menu()

def clone_menu():
    print("\n===== Cloning menu =====")
    # Each inserted disc will be cloned to a new ISO in the specified directory
    print("1: Continuous clone")
    # One job for one disc will be added
    print("2: Single clone job")
    choice = str(input("> "))
    if choice == "..":
        main_menu()
    elif choice == "h":
        main_menu()
    elif choice == "q":
        sys.exit()
    elif choice == "1":
        clone_stuff.cont_clone_menu()
    elif choice == "2":
        clone_stuff.add_clone_job_menu()

def erase_menu():
    print("\n===== Erase menu =====")
    print("1: Continuous erase")
    print("2: Single erase")
    choice = str(input("> "))
    if choice == "..":
        main_menu()
    elif choice == "h":
        main_menu()
    elif choice == "q":
        sys.exit()
    elif choice == "1":
        erase_stuff.cont_erase_menu()
    elif choice == "2":
        erase_stuff.add_erase_job_menu()

def burn_menu():
    # TODO: Burn menu (ISO > CD/DVD/BD)
    # 2 options:
    # One file to all discs
    # One file to one disc (just one job, multiple jobs can run at the same time)
    pass
