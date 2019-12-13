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
        print(self.description)
        print("You can move to these locations: ", end="")
        print(self.get_northern(), end=", ")
        print(self.get_southern(), end=", ")
        print(self.get_eastern(), end=", ")
        print(self.get_western(), end=".")
        return "{}\nYou can move to these locations: {} (north) {} (south) {} (east) {} (west)".format(self.description, self.get_northern(), self.get_southern(), self.get_eastern(), self.get_western())
        
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

castle = Castle("Castle", "The walls are covered in moss. It looks deserted. There is a big doorway.", None, None, "forest1")
forest1 = Location("Forest", "You entered the forest. It seems like you are on the outskirt of it. You also see an old road.", None, None, "forest_split", "castle")
forest_split = Location("Forest split", "You arrive at a split. One road heads to the west. The other one heads east. There are no markings or signs. You only see that the eastern road looks newer." , None, "forest2", "forest3", "castle")
forest3 = Location("Forest", "You venture deeper into the forest. You follow the road which seems to be well maintained and still used.", None, None, "lake", "forest_split")
lake = Location("Lake", "You come out of the forest and see a big lake.", None, None, None, "forest3")
forest2 = Location("Forest", "You enter a forest. You used to go here with your father when he was still alive. You have tons of memories about this place.", "forest_split", None, "house")
house = Location("House", "This is the house where you grew up. You have many memories of this place.", None, None, None, "forest2")

castle.eastern_slot = forest1
forest1.eastern_slot = forest_split
forest1.western_slot = castle
forest_split.southern_slot = forest2
forest_split.eastern_slot = forest3
forest_split.western_slot = castle
forest3.eastern_slot = lake
forest3.western_slot = forest_split
lake.western_slot = forest3
forest2.northern_slot = forest_split
forest2.eastern_slot = house
house.western_slot = forest2

class Player:
    def __init__(self):
        self.current_location = house
    def __str__(self):
        return "I am currently at the {} location".format(self.current_location)
    def move(self, where_to):
        if where_to == "north" and self.current_location.get_northern_slot is not None:
            self.current_location = self.current_location.get_northern_slot
        elif where_to == "south" and self.current_location.get_southern_slot is not None:
            self.current_location = self.current_location.get_southern_slot
        elif where_to == "east" and self.current_location.ger_eastern_slot is not None:
            self.current_location = self.current_location.get_eastern_slot
        elif where_to == "west" and self.current_location.get_western_slot is not None:
            self.current_location = self.current_location.get_western_slot
        else:
            print("You can't move here!")
            print("Please choose a different location")
    def print_current_location(self):
        return self.current_location

player1 = Player()

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
