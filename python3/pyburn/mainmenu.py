import erase_stuff
import clone_stuff
import sys

def main_menu():
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
    print("1: Continuous clone")
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
