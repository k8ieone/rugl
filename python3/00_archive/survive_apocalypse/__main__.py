import char_gen
import random

class Survivor:
    def __init__(self, name, personality, temperament):
        self.name = name
        self.personality = personality
        self.temperament = temperament
        self.town = "smt"

        self.thirst = random.randrange(0, 10)
        self.hunger = random.randrange(0, 10)
        # Does the character start with random items or empty inventory
        self.inventory = {}
    def __str__(self):
        return "I am a human"
        # return "This is {0}. He is from {1}. He is an {2} and a {3}. He was {4} before the apocalipse started".format(self.name, self.town, self.personality, self.temperament, self.former_job)

# Let's just start testing stuff...

some_temp_var = char_gen.generate_character()
david = Survivor("David", some_temp_var[0], some_temp_var[1])
print(david)
