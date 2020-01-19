import random

def write_file(number_of_entries):
    with open("text.txt", "w") as f:
        for i in range(number_of_entries):
            f.write(str(random.randint(1, 100)) + "\n")
            
write_file(50)

def read_file():
    list_of_numbers = []
    with open("text.txt", "r") as f:
        list_of_numbers = f.readlines()
    
    # Strip out the \ns
    for thing in list_of_numbers:
        newlist.append(thing.strip())

print(read_file())