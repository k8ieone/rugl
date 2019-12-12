#!/usr/bin/env python

class Fighter:
    def __init__(self, myName, level, points, lives):
        self.myName = myName
        self.level = level
        self.points = points
        self.lives = lives
    def __str__(self):
        return "idk"

class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
    def score(self):
        if self.fighter1.level > self.fighter2.level:
            self.fighter1.points += 2
            self.fighter2.lives -= 1
        elif self.fighter2.level > self.fighter1.level:
            self.fighter2.points += 2
            self.fighter1.lives -= 1
        elif self.fighter1.level == self.fighter2.level:
            self.fighter1.points += 1
            self.fighter2.points += 1
        return "Fighter 1: Fighter {} has {} lives and got {} points.\nFighter 2: Fighter {} has {} lives and got {} points.".format(self.fighter1.myName, self.fighter1.lives, self.fighter1.points, self.fighter2.myName, self.fighter2.lives, self.fighter2.points)
    def __str__(self):
        return self.score()

wizard = Fighter("wizard", 40, 100, 4)
monster = Fighter("monster", 40, 100, 1)
fight = Fight(wizard, monster)
print(fight)
