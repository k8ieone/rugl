import random

game = True

class Location:
    def __init__(self, name, description, northern_slot=None, southern_slot=None, eastern_slot=None, western_slot=None):
        self.name = name
        self.description = description
        self.northern_slot = northern_slot
        self.southern_slot = southern_slot
        self.eastern_slot = eastern_slot
        self.western_slot = western_slot
        
    def get_northern(self):
        return self.northern_slot
    def get_southern(self):
        return self.southern_slot
    def get_eastern(self):
        return self.eastern_slot
    def get_western(self):
        return self.western_slot
    
    def __str__(self):
        print("You can move to there locations: ", sep="")
        print(get_northern, sep=", ")
        print(get_southern, sep=", ")
        print(get_eastern, sep=", ")
        print(get_western, sep=".")
        
class Castle(Location):
    def explore(self):
        random_number = random.randrange(0, 100)
        if random_number > 50:
            print("You found treasure!")
            print("You won the game!")
            game = False
        if random_number <= 50:
            print("You got lost in the castle...")
            print("You loose!")
            game = False

class Player:
    def __init__(self):
        self.current_location = house
    def __str__(self):
        return "I am currently at the {} location".format(self.current_location)
    def move(self, where_to):
        if where_to == "north" and self.current_location.get_northern_slot != None:
            self.current_location = self.current_location.get_northern_slot
        elif where_to == "south" and self.current_location.get_southern_slot != None:
            self.current_location = self.current_location.get_southern_slot
        elif where_to == "east" and self.current_location.ger_eastern_slot != None:
            self.current_location = self.current_location.get_eastern_slot
        elif where_to == "west" and self.current_location.get_western_slot != None:
            self.current_location = self.current_location.get_western_slot
        else:
            print("You can't move here!")
            print("Please choose a different location")

castle = Castle("Castle", "The walls are covered in moss. It looks deserted. There is a big doorway.", None, None, "forest1")
forest1 = Location("Forest", "You entered the forest. It seems like you are on the outskirt of it. You also see an old road.", None, None, "forest_split", "castle")
forest_split = Location("Forest split", "You arrive at a split. One road heads to the west. The other one heads east. There are no markings or signs. You only see that the eastern road looks newer." , None, "forest2", "forest3", "castle")

while game is True:
    print(player1.current_location)
    player_input = str(input("Enter a command: "))
    if "Move" in player_input:
        if "north" in player_input:
            player1.move("north")
        elif "south" in player_input:
            player1.move("south")
        elif "east" in player_input:
            player1.move("east")
        elif "west" in player_input:
            player1.move("west")
    elif "End" in player_input:
        game = False