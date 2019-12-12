#!/usr/bin/env python

class Team:
    def __init__(self, teamName, points, fightCount):
        self.teamName = teamName
        self.points = points
        self.fightCount = fightCount
    def __str__(self):
        return "Team {} played {} fights and got {} points.".format(self.teamName, self.points, self.fightCount)
    
class Fight:
    def __init__(self, homePlayers, guestPlayers, goalsHome, goalsGuests):
        self.homePlayers = homePlayers
        self.guestPlayers = guestPlayers
        self.goalsHome = goalsHome
        self.goalsGuests = goalsGuests
    def vyhodnoceni(self):
        self.homePlayers.fightCount += 1
        self.guestPlayers.fightCount += 1
        if self.goalsHome > self.goalsGuests:
            self.homePlayers.points += 2
        elif self.goalsHome < self.goalsGuests:
            self.goalsGuests.points += 2
        elif self.goalsGuests == self.goalsHome:
            self.goalsGuests.points += 1
            self.goalsHome.points += 1
        return "Home team: Team {} has played {} fights and got {} points.\nGuest team: Team {} has played {} fights and got {} points.".format(self.homePlayers.teamName, self.homePlayers.fightCount, self.homePlayers.points, self.guestPlayers.teamName, self.guestPlayers.fightCount, self.guestPlayers.points)
    def __str__(self):
        return self.vyhodnoceni()

sheep = Team("Sheep", 2, 1)
wolves = Team("Wolves", 1, 2)
fight = Fight(sheep, wolves, 3, 1)
print(fight)
